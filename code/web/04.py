#!/usr/bin/env python3

from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/")
def index():
    with open("./html/index.html") as f :
        res = f.read()
    return res


@app.route("/test")
def test():
    return "TEST PAGE"


@app.route("/html")
def html_code():
    with open('./html/html.html') as f :
        res = f.read()
    return res 


@app.route("/request")
def request_test():
    led1_val = request.args.get("led1")

    if(led1_val in ("on","off")):
        print("led 1 : %s" % led1_val)
        ## do GPIO action here
        return "led 1 ok"

    return "not ok"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
