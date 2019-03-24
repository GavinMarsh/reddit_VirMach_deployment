#! usr/bin/env python3
import praw
from pymongo import MongoClient
import json
from datetime import datetime
import logging


# setting model to local instance of MongoDB
##MONGO_HOST = 'mongodb://localhost:27017/gm_sandbox'

# setting model to MongoDB Atlas
MONGO_HOST = "mongodb+srv://gavin:P_12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true"
client = MongoClient(MONGO_HOST)
db = client.gm_sandbox

# stting the var reddit equal to consumer keys and access tokens, used for PRAW OAuth
reddit = praw.Reddit(client_id='5LkylQ5qPyJgQQ', \
                     client_secret='qjslGAi3yupCKHiRDseg4U13hKc', \
                     user_agent='reddit-top-posts', \
                     username='reslondoner', \
                     password='1A*U5Ql51nXGlt#li5Fqlo0Ye*7SoCGL%@n$g3hA3ry79G96NL$XMeNc0o&wZTMO4n9mgAznHAmJi')

# function that collects posts from subreddit
def Collect(sub_name):
    #subreddit = reddit.subreddit('eos').top('week')
    subreddit = reddit.subreddit(sub_name).top('week')
    # creating document:
    for post in subreddit:
        utc_date = post.created_utc
        parsed_date = datetime.utcfromtimestamp(utc_date)

        data = {
            'title': post.title,
            'date': utc_date,
            'date_str': parsed_date.strftime('%Y-%m-%d'),
            'score': post.score,
            'url': post.url,
            'sub': str(post.subreddit),
            'commentsUrl': post.url
            #'author': str(post.author)

            }
        # inserting documents into MongoDB collection.
        if post.score > 5:
            db.top_reddit_posts.insert_one(data)

    return()

# flushing collection before inserting new documents
db.top_reddit_posts.drop()

# calling Collect function for each required subreddit.
Collect('eos')
Collect('python')
Collect('datascience')
Collect('programming')
Collect('machinelearning')
