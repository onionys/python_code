#!/usr/bin/env python3

from RPi import GPIO as gp
from time import sleep

class I2CDev:

    def __init__(self,addr,sda_pin = 3,scl_pin = 5):
        self.addr = addr
        self.sda_pin = sda_pin
        self.scl_pin = scl_pin
        if(gp.getmode() != 10):
            gp.setmode(gp.BOARD)
        gp.setup(self.sda_pin,gp.OUT)
        gp.setup(self.scl_pin,gp.OUT)
        gp.output(self.sda_pin,1)
        gp.output(self.scl_pin,1)

    def clk_one(self):
        gp.output(self.scl_pin,1)
        gp.output(self.scl_pin,0)

    def get_sda_lv(self):
        return gp.input(self.sda_pin)

    def get_scl_lv(self):
        return gp.input(self.scl_pin)

    def s_bit(self):
        scl_lv = self.get_scl_lv()
        sda_lv = self.get_sda_lv()

        if(scl_lv == 1):
            if(sda_lv == 0):
                gp.output(self.scl_pin,0)
                gp.output(self.sda_pin,1)
                gp.output(self.scl_pin,1)
            elif(sda_lv == 1):
                pass
            else:
                print("ERROR I2C SBIT")
                return -1
        elif(scl_lv == 0):
            gp.output(self.sda_pin,1)
            gp.output(self.scl_pin,1)
        else:
            print("ERROR I2C SBIT")
            return -1

        gp.output(self.sda_pin,0)
        gp.output(self.scl_pin,0)


    def p_bit(self):

        if(self.get_scl_lv() == 1):
            print("I2C ERROR P_BIT: SCL_LV IS HIGH")
            return -1

        # now scl_lv == 0
        if(self.get_sda_lv() == 1):
            gp.output(self.sda_pin,0)
        gp.output(self.scl_pin,1)
        gp.output(self.sda_pin,1)

    def send_bit(self,val):
        gp.output(self.sda_pin, val)
        self.clk_one()

    def recv_bit(self):
        gp.output(self.scl_pin,0)
        res = self.get_sda_lv()
        self.clk_one()
        return res 

    def send_byte(self,val):
        self.send_bit(1 if val & 0b10000000 else 0)
        self.send_bit(1 if val & 0b01000000 else 0)
        self.send_bit(1 if val & 0b00100000 else 0)
        self.send_bit(1 if val & 0b00010000 else 0)
        self.send_bit(1 if val & 0b00001000 else 0)
        self.send_bit(1 if val & 0b00000100 else 0)
        self.send_bit(1 if val & 0b00000010 else 0)
        self.send_bit(1 if val & 0b00000001 else 0)

    def recv_byte(self):
        gp.setup(self.sda_pin,gp.IN)
        val  = self.recv_bit() << 7
        val |= self.recv_bit() << 6
        val |= self.recv_bit() << 5
        val |= self.recv_bit() << 4
        val |= self.recv_bit() << 3
        val |= self.recv_bit() << 2
        val |= self.recv_bit() << 1
        val |= self.recv_bit()
        gp.setup(self.sda_pin,gp.OUT)
        return val

    def send_ack(self):
        gp.output(self.sda_pin, 0)
        self.clk_one()
        gp.output(self.sda_pin, 1)

    def send_noack(self):
        gp.output(self.sda_pin, 1)
        self.clk_one()

    def recv_ack(self):
        gp.output(self.sda_pin,1)
        gp.setup(self.sda_pin,gp.IN)
        res = self.get_sda_lv()
        self.clk_one()
        gp.setup(self.sda_pin,gp.OUT)
        return res

    def get_reg(self,reg,size=1):
        res = [0 for i in range(size)]

        self.s_bit()

        self.send_byte(self.addr << 1 | 0x00)
        if(self.recv_ack()==1):
            return -1

        self.send_byte(reg)
        if(self.recv_ack()==1):
            return -1

        self.s_bit()

        self.send_byte(self.addr << 1 | 0x01)
        if(self.recv_ack()==1):
            return -1

        for i,v in enumerate(res):
            val = self.recv_byte()
            if(i == (len(res)-1)):
                self.send_noack()
            else:
                self.send_ack()
            if(val == -1):
                return -1
            res[i] = val
        self.p_bit()
        return res


class Si7020(I2CDev):

    def __init__(self):
        super(Si7020,self).__init__(0x40)

    def read_reg_hold_master_mode(self,reg):

        self.s_bit()

        self.send_byte( self.addr << 1 | 0x00)
        if( self.recv_ack() == 1):
            print("I2C ERROR: No ack : %d" % self.addr)
            return -1

        self.send_byte(reg)
        if(self.recv_ack() == 1):
            print("I2C ERROR: No ack : %d" % self.addr)
            return -1

        self.s_bit()

        self.send_byte( self.addr << 1 | 0x01)
        if(self.recv_ack() == 1):
            print("I2C ERROR: No ack : %d" % self.addr)
            return -1

        sleep(0.02)

        MS_byte = self.recv_byte()
        self.send_ack()

        LS_byte = self.recv_byte()
        self.send_noack()
        self.p_bit()
        return (MS_byte, LS_byte)


    def read_RH(self):
        res = self.read_reg_hold_master_mode(0xE5)
        if(res == -1):
            return -1

        MS_byte , LS_byte = res[0], res[1]
        rh_val = MS_byte << 6 | LS_byte >> 2
        return 125 * rh_val / 65536 - 6

    def read_temperature(self):
        res = self.read_reg_hold_master_mode(0xE3)
        if(res == -1):
            return -1
        val =  (res[0] << 8) | res[1]

        return 175.72*val/65536 - 46.85

    def get_data(self):
        rh = self.read_RH()
        temp = self.read_temperature()
        return(rh,temp)

if __name__ == "__main__":
    si = Si7020()
    for i in range(100):
        sleep(0.5)
        print(si.get_data())


