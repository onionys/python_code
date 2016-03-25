#!/usr/bin/env python3
from spidev import SpiDev
from time import sleep
import state_machine as sm
from cc2500 import CC2500


class CC2500sm(CC2500):
    def __init__(self):
        super(self,CC2500).__
