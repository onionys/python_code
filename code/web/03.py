#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/test")
def test():
    return "TEST PAGE"

@app.route("/html")
def html_code():
    with open('./html/html.html') as f :
        res = f.read()
    return res 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
