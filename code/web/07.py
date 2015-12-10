#!/usr/bin/env python3

import os
from flask import Flask
from flask import request
from flask import send_from_directory
import edu

app = Flask(__name__)

led1 = edu.led(13)
led2 = edu.led(15)
btn1 = edu.button(16)
btn2 = edu.button(18)
buzzer = edu.buzzer(32)
relay = edu.relay(11)


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

@app.route("/led2/<value>")
def led2_val(value):
    if value == "on":
        print("led2 on")
        return "ok"
    elif value == "off":
        print("led2 off")
        return "ok"

    return "not ok"


@app.route("/button1")
def button1_html():
    return str(btn1.read())

@app.route("/button2")
def button2_html():
    return str(btn2.read())


@app.route("/file/<path:filename>")
def send_my_file(filename):
    return send_from_directory('./file',filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
