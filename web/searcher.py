#!/usr/bin/python3

from flask import Flask, request
import json
import re
import pymongo
from run import config, app, zbrunk_db, events_collection, searcher_auth_tokens

@app.route('/services/searcher', methods=['POST'])
def search():
    if request.method == 'POST':
        status_ok = True
        data_string = list(request.form)[0]
        print(data_string)
        events = list()

        # Example:
        #curl -k https://127.0.0.1:8088/services/searcher \
        # -d '{"search": "query", "output_mode": "json", "max_count":"10000000",
        #               "auth_token":"8DEE8A67-7700-4BA7-8CBF-4B917CE23512"}'

        search_params = dict()
        try:
            search_params = json.loads(data_string)
        except:
            text = "Data parsing failure"  # check codes and messages!
            code = 3
            status_ok = False

        auth_token = ""
        if search_params != dict():
            if 'auth_token' in search_params:
                auth_token = search_params['auth_token']
            if not auth_token in searcher_auth_tokens:
                text = "Authentication Error"  # check codes and messages!
                code = 2
                status_ok = False

        if status_ok == True:
            text = "Success"
            events = search_params['search']
            code = 0
            results = list()
            for event in events_collection.find({"$and": [
                    {"event_type": {"$eq": search_params['search']["event_type"]}},
                    {"time": {"$gte": search_params['search']["time"]["from"]}},
                    {"time": {"$lte": search_params['search']["time"]["to"]}}
            ]}):
                event['_id'] = str(event['_id'])
                results.append(event)

        return json.dumps({'results': results, 'text':text, 'code':code})