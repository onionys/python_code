#!/usr/bin/env python3
from spidev import SpiDev
from time import sleep

class CC2500(object):

    REG_MARCSTATE = 0xC0 | 0x35
    CMD_SRES = 0x30
    CMD_SFSTXON = 0x31
    CMD_SXOFF = 0x32
    CMD_XCAL = 0x33
    CMD_SRX  = 0x34
    CMD_STX  = 0x35
    CMD_SIDLE = 0x36
    CMD_SWOR = 0x38
    CMD_SPWD = 0x39
    CMD_SFRX = 0x3A
    CMD_SFTX = 0x3B
    CMD_SWORRST = 0x3C
    CMD_SNOP = 0x3D
    CMD_PATABLE = 0x3E
    CMD_TXFIFO = 0x3F

    CMD_SINGLE_WRITE = 0x00
    CMD_BRUST_WRITE = 0x40
    CMD_SINGLE_READ  = 0x80
    CMD_BRUST_READ = 0xC0

    # get Main Radio Control State Machine State
    def __init__(self, bus = 0, channel_select = 1):
        self.bus = SpiDev()
        self.bus.open(bus,channel_select)
        self.reset()

    ## 
    ## COMMAND  
    ##
    def STX(self):
        self.bus.xfer2([self.CMD_STX])

    def SRX(self):
        self.bus.xfer2([self.CMD_SRX])

    def SIDLE(self):
        self.bus.xfer2([self.CMD_SIDLE])

    def SFRX(self):
        self.bus.xfer2([self.CMD_SFRX])
    
    def SFTX(self):
        self.bus.xfer2([self.CMD_SFTX])

    def SRES(self):
        self.bus.xfer2([self.CMD_SRES])

    ## Access REG

    def get_STATE(self):
        return self.bus.xfer2([0xC0 | 0x35, 0x00])[1]

    def get_RXBYTES(self):
        return self.bus.xfer2([0xC0 | 0x3B, 0x00])[1]


    def write_TXFIFO(self,package):
        tmp = []
        if type(package) == str:
            tmp = [ord(i) for i in package]
        else:
            tmp = list(package)
        tmp = [self.CMD_TXFIFO | self.CMD_BRUST_WRITE ,len(tmp)] + tmp
        self.bus.xfer2(tmp)    # write package to fifo buffer (max 64byte)


    def read_RXFIFO(self):
        len_FIFO = self.get_RXBYTES()
        return self.bus.xfer2([self.CMD_BRUST_READ | 0x3F for i in range(len_FIFO)])


    def reset(self):
        self.SRES()

        reg_config = [
            0x29,0x2E,0x06,0x07,0xD3,0x91,0x61,0x04,
            0x45,0x00,0x00,0x09,0x00,0x5E,0xC4,0xEC,
            0x2C,0x22,0x73,0x22,0xF8,0x01,0x07,0x00,
            0x18,0x1D,0x1C,0xC7,0x00,0xB2,0x87,0x6B,
            0xF8,0xB6,0x10,0xEB,0x0B,0x1D,0x11,0x41,
            0x00,0x59,0x7F,0x3C,0x88,0x31,0x0B
        ]

        for reg, val in enumerate(reg_config):
            self.bus.xfer2([reg, val])

        self.SIDLE()
        self.SFRX()
        self.SFTX()

    ## USER API

    def write(self,package):
        self.write_TXFIFO(package)
        if(self.get_STATE() == 22):
            self.SFTX()
            self.SIDLE()
            return -1
        self.STX()
        return 0

    def read(self):
        self.reset()
        self.SRX()
        while(True):
            sleep(0.1)
            state = self.get_STATE()
            if(state in [13,14,15]):
                continue
            elif(state == 1):
                res = self.read_RXFIFO()
                return res
            elif(state == 17):
                self.SFRX()
                self.SIDLE()
                return -1


if __name__ == "__main__":
    from time import sleep
    cc = CC2500()
    count = 0
    while True:
        cc.write("hello",count)
        count += 1
        if count % 100 == 0:
            cc.reset()
    
