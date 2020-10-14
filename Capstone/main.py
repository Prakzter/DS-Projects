import os
import googleapiclient.discovery
from csv import writer, DictWriter
import pandas as pd
import numpy as np
from creds import api_key
from isodate import parse_duration, parse_datetime

from YT_api import get_comments, get_video_stats




def main():
 
    data = pd.read_csv('cleaned_vidlist.csv')
 
    get_video_stats(data)
    get_comments(data)

        



if __name__ == "__main__":
    main()

