#!/usr/bin/python3

# We need here a flask-based service that will get events from user and put them in Mongodb

# pip3 install flask

from flask import Flask, request
import json

auth_tokens = {"8DEE8A67-7700-4BA7-8CBF-4B917CE2352B": {"index": "test_index"}}

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, it's Zbrunk!"


@app.route('/services/collector', methods=['POST'])
def collect():
    if request.method == 'POST':
        status_ok = True

        headers = request.headers
        data = request.form
        auth_token = ""
        index = ""
        auth_header = headers.get('Authorization').split(" ")
        if len(auth_header) > 1:
            auth_token = auth_header[1]
        print(auth_token)
        print(data)

        if not auth_token in auth_tokens:
            text = "Authentication Error" # check codes and messages!
            code = 2
            status_ok = False
        else:
            index = auth_tokens[auth_token]['index']

        if status_ok:
            text = "Success"
            code = 0

        return json.dumps({"text": text, "code": code})



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8088, ssl_context=('cert/certificate.pem', 'cert/key.pem'), debug=True)


