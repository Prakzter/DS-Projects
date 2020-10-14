import os
import googleapiclient.discovery
from csv import writer, DictWriter
import pandas as pd
import numpy as np
from creds import api_key
from isodate import parse_duration, parse_datetime



# ------------- for searching of video_ids --------------

videoid_dict = {}
maxresults = 10
cycles = 8

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = api_key
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

request_search = youtube.search().list(
    part="snippet",
    maxResults=maxresults,
    type="video",
    # order='viewCount',
    relevanceLanguage="en",
    q="Secretlab chair review -game"
)
response_search = request_search.execute()['items']


counter = 0
for x in range(cycles):
    if x > 0:
        nextpage = request_search.execute()['nextPageToken']
        request_search = youtube.search().list(
            part="snippet",
            maxResults=maxresults,
            relevanceLanguage="en",
            type="video",
            # order='viewCount',
            pageToken=nextpage,
            q="Secretlab chair review -game" 
            )
        response_search = request_search.execute()['items']
        


    for response in response_search:
        
        temp_dict = {}

        video_id = response['id']['videoId']
        video_title = response['snippet']['title']
        video_date = parse_datetime(response['snippet']['publishedAt'])
        

        temp_dict['video_id'] = video_id
        temp_dict['video_title'] = video_title
        temp_dict['video_date'] = video_date
        videoid_dict[counter] = temp_dict

        counter += 1
    print(counter, "videos retrieved")

    nextpage = request_search.execute()['nextPageToken']



print('------- SEARCH ENDED --------')
df = pd.DataFrame.from_dict(videoid_dict, orient='index')
df.to_csv(f'videoidlist_{nextpage}.csv', index=False)

# ------------------------------------------------------------------------    



# ------- code for getting video stats -------
def get_video_stats(data):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = api_key
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

    with open('vidstats.csv', 'a+') as f:
        fieldnames = ['video_id','video_date','video_title','video_author','video_tags','video_duration','viewCount','likeCount','dislikeCount','favoriteCount','commentCount']
        csv_writer = DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

    for index, row in data.iterrows(): 
        vId = row['video_id']
       
        request_stats = youtube.videos().list(
            part="snippet,localizations,statistics,contentDetails",
            id=vId
            )
        response_stats = request_stats.execute()['items']



        for response in response_stats:
            try:
                vt_draft = response['snippet']['tags']
                vt_final = ','.join(vt_draft)
            except:
                vt_final = np.nan
                
            try:
                lc = response['statistics']['likeCount']
            except:
                lc = np.nan

            try:
                dc = response['statistics']['dislikeCount']
            except:
                dc = np.nan
                

            with open('vidstats.csv', 'a+') as f:
                fieldnames = ['video_id','video_date','video_title','video_author','video_tags','video_duration','viewCount','likeCount','dislikeCount','favoriteCount','commentCount']
                csv_writer = DictWriter(f, fieldnames=fieldnames)
                csv_writer.writerow({'video_id' : vId,
                                    'video_date': parse_datetime(response['snippet']['publishedAt']) ,
                                    'video_title': response['snippet']['title'],
                                    'video_author' : response['snippet']['channelTitle'],
                                    'video_tags' : vt_final,
                                    'video_duration' : parse_duration(response['contentDetails']['duration']),
                                    'viewCount' : response['statistics']['viewCount'],
                                    'likeCount' : lc,
                                    'dislikeCount' : dc,
                                    'favoriteCount' : response['statistics']['favoriteCount'],
                                    'commentCount' : response['statistics']['commentCount'] 
                                    })
        print(f'Scraping stats from video {index+1} of {len(data.index)} completed')
    
    print('====='*10, 'Video stats have been collected', '====='*10 )

# -----------------------------------------------------------------------



# ------- code for getting comments -------
def get_comments(data):
        # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = api_key
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
    
    with open('videocomments.csv', 'a+') as f:
        fieldnames = ['videoid', 'comment', 'comment_likes', 'comment_author', 'comment_date','comment_reply', 'reply_author', 'reply_likes', 'reply_date']
        csv_writer = DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

    for index, row in data.iterrows(): 
        vId = row['video_id']

        response = youtube.commentThreads().list(
                part="snippet, replies",
                maxResults=100,
                textFormat='plainText',
                videoId=vId
            ).execute()
                        

        while response: # this loop will continue to run until you max out your quota
                        
            for item in response['items']:
                    
                reply_count = item['snippet']['totalReplyCount']
                if reply_count > 0:
                    for reply in item['replies']['comments']:
                        comment_reply = reply['snippet']['textOriginal']
                        reply_author = reply['snippet']['authorDisplayName']
                        reply_likes = reply['snippet']['likeCount']
                        reply_date = parse_datetime(reply['snippet']['publishedAt'])

                        videoid = item['snippet']['videoId']
                        comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
                        comment_likes = item['snippet']['topLevelComment']['snippet']['likeCount']
                        comment_author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                        comment_date = parse_datetime(item['snippet']['topLevelComment']['snippet']['publishedAt'])

                            #7 write line by line
                        with open(f'videocomments.csv', 'a+') as f:
                            csv_writer = writer(f)
                            csv_writer.writerow([videoid, comment, comment_likes, comment_author,comment_date,comment_reply, reply_author, reply_likes, reply_date])

                            
                else:
                    comment_reply, reply_author, reply_likes, reply_date = np.nan, np.nan, np.nan, np.nan
                
                    videoid = item['snippet']['videoId']
                    comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
                    comment_likes = item['snippet']['topLevelComment']['snippet']['likeCount']
                    comment_author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                    comment_date = parse_datetime(item['snippet']['topLevelComment']['snippet']['publishedAt'])

                    #7 write line by line
                    with open(f'videocomments.csv', 'a+') as f:
                        csv_writer = writer(f)
                        csv_writer.writerow([videoid, comment, comment_likes, comment_author,comment_date,comment_reply, reply_author, reply_likes, reply_date])
                
                #8 check for nextPageToken, and if it exists, set response equal to the JSON response
            if 'nextPageToken' in response:
                response = youtube.commentThreads().list(
                part="snippet, replies",
                maxResults=100,
                textFormat='plainText',
                videoId=vId,
                pageToken=response['nextPageToken']
                ).execute()
            else:
                break

            #9 print out our data of interest
        print(f'Scraping comments from video {index+1} of {len(data.index)} completed')

    print('====='*10, 'Video comments have been collected', '====='*10 )

# -----------------------------------------------------------------------

