# Brand Insights for Secretlab

<img src="logo-1.png" width="300"/>


## Problem statement:
Scraping youtube comments to gather topical insights and information that would help Secretlab and their content creators amplify the Seecretlab brand. 
Build a classifier that would be able to sort new comments to key topics serving insights to the product team.

## Executive Summary:
Since its launch in 2005, YouTube has quickly become the largest video sharing platform on the Internet. As of the year 2016, YouTube has reported more than a billion users with over 300 hours of video uploaded every minute. However, as with other forms of social media, a mountain of insights can be obtained through video analytics and the comments to a brand understand how their consumers are interacting with their products and/or services.

Our main objective is to help Secretlab effectively understand the needs and concerns of their viewers, thus respond faster to these concerns and deliver higher-quality content. These insights could be shared with content creators when representing Secretlab, as part of the media kit. A dataset of 9480 comments sampled from 184 YouTube videos were used to conduct our analysis.


## Insights and recommendation:
* The EDA provided valuable insights from the video statistics that would help content creators in boosting the Secretlab brand, for eg. the time/day to post up content based on engagement, the optimal duration of their video
* Explored the Youtube marketing efforts between the launch of the 2018 series and the 2020 series
* Looked at the effect the length of the comment had on its engagement
* Identified top 3 content creators under the Super, Micro and Nano Influencer categories that Secretlab could potentially collaborate with
* Explored the response time of between comments and replies
* Suggested top 5 keywords that content creators could add to their video tags and improve the SEO of their video
* Analysed key trigger words that viewers associated with the Secretlab brand in their comments
* Using LDA, clustered the comments into top 6 topics    
* Using Doc2Vec and Logistic Regression, created a comment classifier that could be utilised to tag new incoming comments and extract specific product feature feedback

### Topics generated from LDA:
|Topic #| Topic Meaning|
|-------|--------------|
|Topic 0|Firmness of the seat causing back issues|
|Topic 1|Discussion on how long the chair lasts for|
|Topic 2|Considering between Fabric and Leather|
|Topic 3|How great the Omega chair is|
|Topic 4|Whether the lumbar support is good|
|Topic 5|Compliments that the video help make a purchase decision|


<br></br>
***Future Recommendation:***
1. There is a considerable amount of noise in the corpus due to the presence of comments unrelated to the brand but rather directed at the content creator or other details. A Spam/ham classifier could be built to understand and weed out these irrelevant comments to improve the final model's accuracy.
2. Currently, we are only using the dominant topic as the document id but we could potentially pass in the top 3 topics to improve the semantic understanding of each comment and aid in a better classification between topics.  

### Presentation Deck:
[View slides here](https://github.com/Prakzter/DS-Projects/blob/master/Secretlab_Brand_Insights/GA_Capstone_Prak.pdf)

