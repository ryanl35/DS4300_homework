#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

def postTweet():
    with open("generatedTweets.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # the below statement will skip the first row
        next(csv_reader)
        i=0
        dict = {}
        for lines in csv_reader:
            time = i
            text = lines[3]
            dict = {text:time}
            con.zadd('tweets',dict)
            i += 1

postTweet()
