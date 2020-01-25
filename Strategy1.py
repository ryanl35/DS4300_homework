#!/usr/bin/python

import pandas as pd
import time

def postTweet():
      tweets = pd.read_csv("generatedTweets.csv")
      # tweets = tweets.drop ??
      print("HERE")

      iteration = 0
      for i, row in tweets.iterrows():
        print(row['tweet_text'])
        if iteration == 100:
            break
        iteration += 1

postTweet()
