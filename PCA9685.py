#!/usr/bin/env python

import RPi.GPIO as GPIO
import smbus
import time
from sys import argv

class PCA9685:
    help_msg = '''
    PCA9685 [option]
    option:
        up
        down
        reset
        info

        chon [channel]
        choff [channel]
        allch  [ value:0~4095 ]
        allchd [duty cycle]

        ch   [channel] [value:0~4095]
        chd  [channel] [duty cycle:0.0~100.0]
        rchd  [channel] [relative duty cycle:0.0~100.0]

    command :
    T:(us) --> delay time
    D(ch):(duty cycle: 0.0 ~ 100.0) --> set ch as duty cycle
    C(ch):(count : 0 ~ 4095) --> set ch as count
    ex: 
        'T:100 C1:1024 C15:2035 C13:999 C07:777 D09:55.5'
    '''


    ######################
    # REG POSITION 
    ######################


    __MODE1              = 0x00
    __MODE2              = 0x01
    __SUBADR1            = 0x02
    __SUBADR2            = 0x03
    __SUBADR3            = 0x04
    __PRESCALE           = 0xFE
    __LED0_ON_L          = 0x06
    __LED0_ON_H          = 0x07
    __LED0_OFF_L         = 0x08
    __LED0_OFF_H         = 0x09
    __ALL_LED_ON_L       = 0xFA
    __ALL_LED_ON_H       = 0xFB
    __ALL_LED_OFF_L      = 0xFC
    __ALL_LED_OFF_H      = 0xFD


    ######################
    # MODE1 FUNCTION Bits
    ######################


    __RESTART            = 0x80
    __SLEEP              = 0x10
    __AI                 = 0x20
    __ALLCALL            = 0x01
    __INVRT              = 0x10
    __OUTDRV             = 0x04


    def __init__(self, addr = 0x40, freq=50):
        self.addr = addr
        self.bus = smbus.SMBus(1)  # 1 : /dev/i2c-1
        self.setFreq(freq)
        self.setAutoIncrement(1)


    ###########################
    # GET METHODS:
    ###########################


    def getRegAll(self):
        self.setAutoIncrement(1)
        _reg_0_31 = self.bus.read_i2c_block_data(self.addr, 0, 32)
        _reg_32_63 = self.bus.read_i2c_block_data(self.addr, 32, 32)
        _reg_64_69 = self.bus.read_i2c_block_data(self.addr, 64, 6)
        return _reg_0_31 + _reg_32_63 + _reg_64_69


    def getRegChOnL(self,channel):
        return self.bus.read_byte_data(self.addr, 4 * channel + self.__LED0_ON_H)


    def getRegChOnH(self,channel):
        return self.bus.read_byte_data(self.addr, 4 * channel + self.__LED0_ON_L)


    def getRegChOffL(self,channel):
        return self.bus.read_byte_data(self.addr, 4 * channel + self.__LED0_OFF_L)


    def getRegChOffH(self,channel):
        return self.bus.read_byte_data(self.addr, 4 * channel + self.__LED0_OFF_H)


    def getRegMODE1(self):
        return self.bus.read_byte_data(self.addr, self.__MODE1)


    def getRegMODE2(self):
        return self.bus.read_byte_data(self.addr, self.__MODE2)


    def getRegPrescale(self):
        return self.bus.read_byte_data(self.addr, self.__PRESCALE)


    def getValChOff(self, channel):
        if(not self.isAutoIncrement() ):
            self.setAutoIncrement(1)
        vals = self.bus.read_i2c_block_data(self.addr, self.__LED0_OFF_L + 4 * channel, 2)
        val = vals[0] + ((vals[1] & 0x0f) << 8)
        print val
        return val


    def getValChOn(self, channel):
        if(not self.isAutoIncrement() ):
            self.setAutoIncrement(1)
        vals = self.bus.read_i2c_block_data(self.addr, self.__LED0_ON_L + 4 * channel, 2)
        val = vals[0] + ((vals[1] & 0x0f) << 8)
        print val
        return val


    def getFreq(self):
        _prescale = self.getRegPrescale()
        _osc = 25e6
        _freq = 1./((_prescale + 1) * 4096 / _osc)
        return _freq


    def getChDuty(self, channel ):
        if( (channel < 0)  and (channel > 15)):
            print "error: channel out of range"
            return -1
        #_on, _off = self.getChanON_OFF(channel)
        _on  = self.getRegChOnL( channel) + ( (self.getRegChOnH(channel) & 0x0f ) << 8)
        _off = self.getRegChOffL(channel) + ( (self.getRegChOffH(channel) & 0x0f ) << 8)
        
        if(_on < _off) :
            return ((_off - _on) * 100 ) / 4096.0
        elif(_on > _off):
            return 100.0 - ( ((_on - _off) * 100 ) / 4096.0 )
        else:
            return 0.0


    def getChanON_OFF(self,channel ):
        _led_on_L = self.getRegChOnL(channel)
        _led_on_H = self.getRegChOnH(channel) & 0b00001111

        _led_off_L = self.getRegChOffL(channel)
        _led_off_H = self.getRegChOffH(channel) & 0b00001111

        _led_on  = (_led_on_H  << 8 ) + _led_on_L
        _led_off = (_led_off_H << 8 ) + _led_off_L

        return (_led_on, _led_off)


    def getCh_ms(self, channel):
        if( (channel < 0)  and (channel > 15)):
            print "error: channel out of range"
            return -1
        #_on, _off = self.getChanON_OFF(channel)
        _on = self.getRegChOnL() + ( (self.getRegChOnH() & 0x0f ) << 8)
        _off = self.getRegChOffL() + ( (self.getRegChOffH() & 0x0f ) << 8)
        
        if(_on < _off) :
            return ((_off - _on) * 20.0) / 4096.0
        elif(_on > _off):
            return 20.0 - ( ((_on - _off) * 20 ) / 4096.0 )
        else:
            return 0.0


    ###########################
    # SET METHODS : 
    ###########################

    def setRegChOnL(self,channel,val):
        self.bus.write_byte_data(self.addr, channel * 4 + self.__LED0_ON_L  , val )


    def setRegChOnH(self,channel,val):
        self.bus.write_byte_data(self.addr, channel * 4 + self.__LED0_ON_H  , val  )


    def setRegChOffL(self,channel,val):
        self.bus.write_byte_data(self.addr, channel * 4 + self.__LED0_OFF_L  , val )


    def setRegChOffH(self,channel,val):
        self.bus.write_byte_data(self.addr, channel * 4 + self.__LED0_OFF_H  , val )


    def setRegMODE1(self,val):
        self.bus.write_byte_data(self.addr, self.__MODE1, val) 


    def setRegMODE2(self,val):
        self.bus.write_byte_data(self.addr, self.__MODE2, val) 


    def setRegPrescale(self, _prescale):
        return self.bus.write_byte_data(self.addr, self.__PRESCALE, _prescale )


    def setAutoIncrement(self, val):
        if(val == 1):
            self.setRegMODE1(self.getRegMODE1() | self.__AI)
        elif(val == 0):
            self.setRegMODE1(self.getRegMODE1() &~ (self.__AI))


    def setI2C_Addr(self,addr):
        self.addr = addr


    def setPWM(self, chan, on, off):
        self.setValChOn(chan, on)
        self.setValChOff(chan, off)


    def setValChOn(self, chan, on):

        if((on & 0xf000) > 0):
            print "error : too large value of on"
            return 

        _on_l =     on & 0x00ff
        _on_h = ( ( on & 0xff00 ) >> 8 ) | ( self.getRegChOnH(chan) & 0x10)
        self.setRegChOnL(chan, _on_l )
        self.setRegChOnH(chan, _on_h )


    def setValChOff(self, chan, off):

        if((off & 0xf000) > 0):
            print "error : too large value of off"
            return 

        _off_l =     off & 0x00ff
        _off_h = ( ( off & 0xff00 ) >> 8 ) | ( self.getRegChOffH(chan) & 0x10)

        self.setRegChOffL(chan , _off_l)
        self.setRegChOffH(chan , _off_h)


    def setFreq(self, freq):
        prescale_val = int(25e6/4096/float(freq) -1.0)
        self.sleep()
        self.setRegPrescale(prescale_val)
        time.sleep(0.005)
        self.wakeup()


    def setChCountRelative(self, channel, count_relative):
        off_val = self.getValChOff(channel) + count_relative
        if( ( off_val > 4095) or (off_val < 0) ):
            return
        vals = [off_val&0x00ff, (off_val & 0xff00) >> 8]
        self.bus.write_i2c_block_data(self.addr, self.__LED0_OFF_L + 4 * channel, vals)


    def setChDutyRelative(self, chan, duty):
        _off = self.getValChOff(chan)
        _off_shift = int(4096.0/100.0 * duty)
        _off += _off_shift
        self.setValChOff(chan,_off)


    def setAllCh(self,val):
        vals = []
        for i in range(16):
            self.setValChOff(i, val)


    def setAllChDuty(self,val):
        self.setAllCh(int(val * 4096 / 100))


    # ex: duty_dic = {1:10.0, 2:20.0, 15:30.0}
    def setByDutyDic(self,duty_dic):
        for key in duty_dic:
            if ((key.__class__ == int) and (key >= 0) and (key <= 15)):
                self.chDuty(key, duty_dic[key])


    def setByDutyDicRelative(self,duty_dic_relative):
        for key in duty_dic_relative:
            if ((key.__class__ == int) and (key >= 0) and (key <= 15)):
                self.setChDutyRelative(key, duty_dic[key])


    # ex: count_dic = {1:1024, 2:2048, 15:999}
    def setByCountDic(self, count_dic):
        for key in count_dic:
            if ((key.__class__ == int) and (key >= 0) and (key <= 15)):
                self.setValChOff(key, count_dic[key])


    ##def setByCountDicRelative(self,count_dic_relative):
    ##    for key in count_dic:
    ##        if ((key.__class__ == int) and (key >= 0) and (key <= 15)):
    ##            self.setPWM_ch_off(key, count_dic[key])

    # ex: cmd = 'T:10 C0:1024 D1:7.5 C10:4095'
    # T:10 --> delay 10 us
    # D1:7.5 --> channel 1 set as duty cycle 7.5 %
    # C10:4095 --> channel 10 set as count 4095 
    def setByCommand(self,cmd):
        delay_time_us = 0
        count_dic = {}
        reset_flag = 0

        for i in cmd.split():
            _line = i.split(":")
            if(_line.__len__() != 2):
                continue

            _ch = -1
            _count = -1

            if (i[0] == 'T'):
                delay_time_us = int(i.split(":")[1])

            elif (i[0] == 'C'):
                _ch = int(_line[0][1:])
                _count = int(_line[1])

            elif (i[0] == 'D'):
                _ch = int(_line[0][1:])
                _count = int(float(_line[1]) * 4096.0 / 100.0)
                count_dic[_ch] = _count

            elif( 'RESET' in i ):
                print "RESET"
                reset_flag = 1

        time.sleep(delay_time_us/1000000.0)
        self.setByCountDic(count_dic)
        if(reset_flag):
            self.reset()

    def setByCMDList(self, cmd_list):
        for i in cmd_list:
            self.setByCommand(i)
    

    #############################
    ## READ CONDITION 
    #############################


    def showInfo(self): 
        mode1 = self.getRegMODE1()
        mode2 = self.getRegMODE2()
        prescale = self.bus.read_byte_data(self.addr, self.__PRESCALE)

        print "MODE1: %s" % bin(mode1)[2:].zfill(8)
        print "MODE2: %s" % bin(mode2)[2:].zfill(8)
        print "sleep: %s" % ('yes' if ((mode1 & self.__SLEEP) > 0) else 'no')
        print "prescale: %d" % prescale
        for i in range(16):
            print "ch:%2d duty cycle:%f %s" % (i,self.getChDuty(i), 'on' if (self.isChOn(i)) else 'off')

    def isAutoIncrement(self):
        return True if((self.getRegMODE1() & self.__AI) != 0) else False


    def isChOn(self, channel):
        _val = self.getRegChOffH(channel) & 0b00010000
        return True if (_val == 0) else False


    #########################
    ## CHANGE CONDITION
    #########################


    def reset(self):
        self.bus.write_byte_data(self.addr, self.__ALL_LED_ON_L, 0)
        self.bus.write_byte_data(self.addr, self.__ALL_LED_ON_H, 0)
        self.bus.write_byte_data(self.addr, self.__ALL_LED_OFF_L, 0)
        self.bus.write_byte_data(self.addr, self.__ALL_LED_OFF_H, 0)
        self.bus.write_byte_data(self.addr, self.__MODE2, 0x04)
        self.bus.write_byte_data(self.addr, self.__MODE1, self.__ALLCALL | self.__AI)
        time.sleep(0.005)


    def sleep(self):
        self.setRegMODE1( self.getRegMODE1() | self.__SLEEP)


    def wakeup(self):
        self.setRegMODE1( self.getRegMODE1() &~ self.__SLEEP )


    def chOn(self, ch):
        self.setRegChOffH(ch, self.getRegChOffH(ch) &~(0x10))


    def chOff(self,ch):
        self.setRegChOffH(ch, self.getRegChOffH(ch) | (0x10))


    def chDuty(self, chan, duty):
        if((duty > 100.0)or (duty < 0.0)):
            return
        _off_count = int(4096.0/100.0 * duty)
        self.setValChOff(chan,_off_count)




if __name__=="__main__":
    pwms = PCA9685()

    if(argv.__len__()== 1):
        print pwms.help_msg
    elif(argv.__len__()== 2):
        if(argv[1] == "up"):
            pwms.wakeup()
        elif(argv[1] == "down"):
            pwms.sleep()
        elif(argv[1] == "reset"):
            print "PCA9685 reset"
            pwms.reset()
        elif (argv[1] == "info"):
            pwms.showInfo()
        elif (argv[1] == "allreg"):
            all_reg = pwms.getRegAll()
            for i in range(all_reg.__len__()):
                print "%2d: %02X" % (i,all_reg[i])

    elif(argv.__len__() == 3):
        if(argv[1] == "chon"):
            _ch = int(argv[2])
            pwms.chOn(_ch)
            print "ch on: %d" % _ch
        if(argv[1] == "choff"):
            _ch = int(argv[2])
            pwms.chOff(_ch)
            print "ch off: %d" % _ch
        elif(argv[1] == 'allchd'):
            _duty = float(argv[2])
            pwms.setAllChDuty(_duty)
        elif(argv[1] == 'allch'):
            _val = int(argv[2])
            pwms.setAllCh(_val)

        elif(argv[1] == 'cmd_file'):
            ff = open(argv[2], 'r')
            cmd_lines = ff.readlines()
            ff.close()
            pwms.setByCMDList(cmd_lines)

    elif(argv.__len__() == 4):
        if(argv[1] == "ch"):
            _ch = int(argv[2])
            _val = int(argv[3])
            #pwms.setPWM_ch_off(_ch,_val)
            pwms.setValChOff(_ch, _val)

        elif(argv[1] == "chd"):
            _ch = int(argv[2])
            _val = float(argv[3])
            pwms.chDuty(_ch,_val)

        elif(argv[1]=='rchd'):
            _ch = int(argv[2])
            _val = float(argv[3])
            pwms.setChDutyRelative(_ch, _val)

