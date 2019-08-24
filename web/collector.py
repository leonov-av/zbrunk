#!/usr/bin/python3

# We need here a flask-based service that will get events from user and put them in Mongodb

# pip3 install flask

from flask import Flask, request
import json
import re

auth_tokens = {"8DEE8A67-7700-4BA7-8CBF-4B917CE2352B": {"event_type": "test_event"}}

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, it's Zbrunk!"

@app.route('/services/collector', methods=['POST'])
def collect():
    if request.method == 'POST':
        status_ok = True

        headers = request.headers

        auth_token = ""
        event_type = ""

        # Checking the authentication token and get the corresponding event_type name
        auth_header = headers.get('Authorization').split(" ")
        if len(auth_header) > 1:
            auth_token = auth_header[1]

        if not auth_token in auth_tokens:
            text = "Authentication Error"  # check codes and messages!
            code = 2
            status_ok = False
        else:
            event_type = auth_tokens[auth_token]['event_type']

        # Dealing with the data
        # It's not clear why, but there is no "\n" in Post request data
        # So I make a dirty hack to present this string as a list of dicts
        data_string = list(request.form)[0]
        data_string = re.sub("}[ \t]*{", "},{", data_string)
        data_string = re.sub("^", "[", data_string)
        data_string = re.sub("$", "]", data_string)
        try:
            events = json.loads(data_string)
        except:
            events = list()
            text = "Data parsing failure"  # check codes and messages!
            code = 3
            status_ok = False

        # Adding event_type to the events
        new_events = list()
        for event in events:
            event['event_type'] = event_type
            new_events.append(event)
        events = new_events

        # Validating the events:
        for event in events:
            if not 'time' in event:
                text = "No time parameter"  # check codes and messages!
                code = 3
                status_ok = False
            else:
                try:
                    time = int(event['time'])
                except:
                    text = "Wrong value of time parameter"  # check codes and messages!
                    code = 3
                    status_ok = False
            if not 'host' in event:
                text = "No host parameter"  # check codes and messages!
                code = 3
                status_ok = False
            if not 'event' in event:
                text = "No event parameter"  # check codes and messages!
                code = 3
                status_ok = False

        # Sending events to Mongo
        if status_ok:
            for event in events:
                print(event)

        if status_ok:
            text = "Success"
            code = 0


        return json.dumps({"text": text, "code": code})



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8088, ssl_context=('cert/certificate.pem', 'cert/key.pem'), debug=True)


