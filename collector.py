#!/usr/bin/python3

# We need here a flask-based service that will get events from user and put them in Mongodb

# pip3 install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, it's Zbrunk!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8088, ssl_context=('cert/certificate.pem', 'cert/key.pem'), debug=True)


