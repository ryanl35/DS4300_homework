#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

def postTweet():
    tweetscsv = open("generatedTweets.csv", "r") #opens tweets csv from HW1
    tweetsReader = csv.reader(tweetscsv, delimiter=',')
    next(tweetsReader) #skips the first row
    i = 0 
    dict = {}
    for tweet in tweetsReader:
        index = i
        text = tweet[3]
        dict = {text:index}
        con.zadd('tweets',dict)
        i += 1

postTweet()
