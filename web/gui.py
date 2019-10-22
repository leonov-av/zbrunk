#!/usr/bin/python3

from flask import Flask, request
from flask_admin import Admin
import json
import re
import pymongo
from run import config, app, zbrunk_db, events_collection, searcher_auth_tokens

@app.route('/', methods=['GET'])
def gui():
    if request.method == 'GET':
          f = open("web/templates/index.html")
          search = f.read()
          f.close()
          return search