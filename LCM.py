#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep
from subprocess import check_output

class qc1602a:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.LCD_RS = 38
        self.LCD_RW = 40
        self.LCD_E  = 29
        self.LCD_D4 = 31
        self.LCD_D5 = 33
        self.LCD_D6 = 35
        self.LCD_D7 = 37

        self.CMD_DELAY = 0.0002
        self.CMD_CLEAR_DELAY = 0.001
        self.reset()


    ## LCM 開機設定
    def reset(self):
        # setup the pin out
        GPIO.setup(self.LCD_E,  GPIO.OUT) # E
        GPIO.setup(self.LCD_RS, GPIO.OUT) # RS
        GPIO.setup(self.LCD_RW, GPIO.OUT) # RW
        GPIO.setup(self.LCD_D4, GPIO.OUT) # DB4
        GPIO.setup(self.LCD_D5, GPIO.OUT) # DB5
        GPIO.setup(self.LCD_D6, GPIO.OUT) # DB6
        GPIO.setup(self.LCD_D7, GPIO.OUT) # DB7

        # initialize the level of all pin
        GPIO.output(self.LCD_D4,0)
        GPIO.output(self.LCD_D5,0)
        GPIO.output(self.LCD_D6,0)
        GPIO.output(self.LCD_D7,0)
        GPIO.output(self.LCD_RS,0)
        GPIO.output(self.LCD_RW,0)
        GPIO.output(self.LCD_E,0)
        
        sleep(0.1)
        GPIO.output(self.LCD_E,1)
        sleep(0.000001)
        GPIO.output(self.LCD_E,0)
        sleep(0.000001)

        ### reset the LCD and use the 4 bit (4-lines) mode
        sleep(0.002)
        self.write_cmd(0x03)
        sleep(0.001)
        self.write_cmd(0x03)
        sleep(0.0001)
        self.write_cmd(0x03)
        sleep(0.0001)
        self.write_cmd(0x02)
        sleep(0.0001)
        ### end reset procedure
        
        # function setup 
        self.write_cmd(0x28)
        self.write_cmd(0x0C)
        self.write_cmd(0x01)
        sleep(self.CMD_CLEAR_DELAY)
        self.write_cmd(0x06)


    # 傳"指令"給LCM模組
    def write_cmd(self , cmd ):
        GPIO.output(self.LCD_RS, 0)
        GPIO.output(self.LCD_RW, 0)
        GPIO.output(self.LCD_E , 0)

        # write high 4 bits
        GPIO.output(self.LCD_D7, 1 if 0b10000000 & cmd else 0)
        GPIO.output(self.LCD_D6, 1 if 0b01000000 & cmd else 0)
        GPIO.output(self.LCD_D5, 1 if 0b00100000 & cmd else 0)
        GPIO.output(self.LCD_D4, 1 if 0b00010000 & cmd else 0)

        sleep(0.000001)
        GPIO.output(self.LCD_E, 1)
        sleep(0.000001)
        GPIO.output(self.LCD_E, 0)

        # write low 4 bits
        GPIO.output(self.LCD_D7, 1 if 0b00001000 & cmd else 0)
        GPIO.output(self.LCD_D6, 1 if 0b00000100 & cmd else 0)
        GPIO.output(self.LCD_D5, 1 if 0b00000010 & cmd else 0)
        GPIO.output(self.LCD_D4, 1 if 0b00000001 & cmd else 0)

        sleep(0.000001)
        GPIO.output(self.LCD_E, 1)
        sleep(0.000001)
        GPIO.output(self.LCD_E, 0)
        sleep( self.CMD_DELAY )
        

    # 傳"資料"給LCM模組
    def write_data(self , data):
        GPIO.output(self.LCD_RS, 1)
        GPIO.output(self.LCD_RW, 0)
        GPIO.output(self.LCD_E , 0)

        # write high 4 bits
        GPIO.output(self.LCD_D7, 1 if 0b10000000 & data else 0)
        GPIO.output(self.LCD_D6, 1 if 0b01000000 & data else 0)
        GPIO.output(self.LCD_D5, 1 if 0b00100000 & data else 0)
        GPIO.output(self.LCD_D4, 1 if 0b00010000 & data else 0)

        sleep(0.000001)
        GPIO.output(self.LCD_E, 1)
        sleep(0.000001)
        GPIO.output(self.LCD_E, 0)

        # write low 4 bits
        GPIO.output(self.LCD_D7, 1 if 0b00001000 & data else 0)
        GPIO.output(self.LCD_D6, 1 if 0b00000100 & data else 0)
        GPIO.output(self.LCD_D5, 1 if 0b00000010 & data else 0)
        GPIO.output(self.LCD_D4, 1 if 0b00000001 & data else 0)

        sleep(0.000001)
        GPIO.output(self.LCD_E, 1)
        sleep(0.000001)
        GPIO.output(self.LCD_E, 0)
        sleep( self.CMD_DELAY )


    ## 指令: 移動游標到指定位址
    ## line 1 ~ 1
    ## col  1 ~ 16
    def move(self,line,col):
        _pos = 0x80 + (line-1) * 0x40 + (col-1)
        self.write_cmd(_pos)


    ## 寫入資料到游標目前的位置(寫入後游標自動向後跳一格)
    def write_msg(self,msg):
        if type(msg) == str:
            data = [ord(i) for i in msg]
            for i in data:
                self.write_data(i)
    

    def clear_line_1(self):
        self.move(1,1)
        self.write_msg(' ' * 16)


    def clear_line_2(self):
        self.move(2,1)
        self.write_msg(' ' * 16)



def get_IP_list():
    ip_list = [ i[5:] for i in check_output('ifconfig').decode().split() if 'addr:' in i]
    return [i for i in ip_list if i]



if __name__ == '__main__':
    myLCD = qc1602a()
    myLCD.reset()
    myLCD.clear_line_1()
    while(1):
        ip_list = get_IP_list()

        for i in ip_list :
            myLCD.clear_line_1()
            myLCD.move(1,1)
            myLCD.write_msg(i)
            sleep(1)
