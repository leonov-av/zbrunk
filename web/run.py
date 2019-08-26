#!/usr/bin/python3

# We need here a flask-based service that will get events from user and put them in Mongodb

# pip3 install flask

from flask import Flask, request
from configobj import ConfigObj
import pymongo

configfile = 'zbrunk.conf'
config = ConfigObj(configfile)

app = Flask(__name__)

mongo_client = pymongo.MongoClient(config['DATABASE']['database'],
                                   username=config['DATABASE']['username'],
                                   password=config['DATABASE']['password'])

zbrunk_db = mongo_client["zbrunk"]
events_collection = zbrunk_db["events"]

# Authentication tokens for Zbrunk collector
auth_tokens = {"8DEE8A67-7700-4BA7-8CBF-4B917CE2352B": {"event_type": "test_event"}}

from collector import *

if __name__ == '__main__':
    app.run(host=config['WEB']['host'], 
    	    port=config['WEB']['port'], 
    	    ssl_context=(config['SSL']['cert'], 
    	    	         config['SSL']['key']), 
    	    debug=config['debug'])


