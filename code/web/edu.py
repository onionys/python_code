#!/usr/bin/env python3
from RPi import GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)

class led:
    def __init__(self,pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.pin, 1)

    def off(self):
        GPIO.output(self.pin, 0)

class relay:
    def __init__(self,pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.pin, 1)

    def off(self):
        GPIO.output(self.pin, 0)


class button:
    def __init__(self,pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def read(self):
        return GPIO.input(self.pin)


class buzzer:
    def __init__(self,pin):
        self.pin = pin
        self.off()

    def on(self):
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, 0)

    def off(self):
        GPIO.setup(self.pin, GPIO.IN)



def getip():
    msg = subprocess.check_output(['ifconfig']).decode().split('\n')
    ips = [i.split()[1].split(':')[1] for i in msg if "inet addr:" in i]
    ips.remove('127.0.0.1')
    return ips[0]
