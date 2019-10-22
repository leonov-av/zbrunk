#!/usr/bin/python3

from flask import Flask, request
from configobj import ConfigObj
import pymongo

configfile = 'zbrunk.conf'
config = ConfigObj(configfile)

app = Flask(__name__)

# MongoDB Connection
mongo_client = pymongo.MongoClient(config['DATABASE']['database'],
                                   username=config['DATABASE']['username'],
                                   password=config['DATABASE']['password'])

zbrunk_db = mongo_client["zbrunk"]
events_collection = zbrunk_db["events"]

# Authentication tokens for Zbrunk collector
collector_auth_tokens = {"8DEE8A67-7700-4BA7-8CBF-4B917CE2352B": {"event_type": "test_event"}}
# Authentication tokens for Zbrunk searcher
searcher_auth_tokens = {"8DEE8A67-7700-4BA7-8CBF-4B917CE23512": {"user_name": "test_user",
																 "permissions": ['read','delete']}}

from collector import *
from searcher import *
from gui import *

if __name__ == '__main__':
    app.run(host=config['WEB']['host'], 
    	    port=config['WEB']['port'], 
    	    ssl_context=(config['SSL']['cert'], 
    	    	         config['SSL']['key']), 
    	    debug=config['debug'])


