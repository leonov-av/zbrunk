#!/usr/bin/python3

from flask import Flask, request
from configobj import ConfigObj
import pymongo

configfile = 'zbrunk.conf'
config = ConfigObj(configfile)


# If you are using Jinja2 to render your templates, you will need to add a few lines of code
# to tell Jinja2 to not use the {{ }} syntax to render variables, because we need those
# double-curly-brace symbols for Vue.js.
# https://stackoverflow.com/questions/46214132/how-can-i-combine-vue-js-with-flask
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))

app = CustomFlask(__name__,
			static_url_path='',
            static_folder='static',
            template_folder='templates')

# MongoDB Connection
mongo_client = pymongo.MongoClient(config['DATABASE']['database'],
                                   username=config['DATABASE']['username'],
                                   password=config['DATABASE']['password'])

zbrunk_db = mongo_client["zbrunk"]
events_collection = zbrunk_db["events"]

# Authentication tokens for Zbrunk collector
collector_auth_tokens = {"8DEE8A67-7700-4BA7-8CBF-4B917CE2352B": {"event_type": "test_event"},
                         "8DEE8A67-7700-4BA7-8CBF-4B917CE23441": {}}

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


