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

        return json.dumps({'results': events})