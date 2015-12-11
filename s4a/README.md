# S4A

S4A 是一個在 Arduino的系統之上開發出來的一個專案，主要分為兩個部份:  

- 圖形化程式言語 Scratch 客製化板。
- Arduino 韌體 S4AFirmware16.ino 

目前支援:

- Arduino Diecimila
- Arduino Duemilanove
- Arduino Uno

S4A專案是為了要讓學生能夠透過撰寫圖形化程式語言 Scratch 來直接控制 Arduino。所以在S4A實作了一個 Arduino 的 .ino 檔(我們稱之為韌體)，只要將之上傳到Arduino的板子上之後，就可以用 S4A 所客製化過的 Scratch 來和其溝通。國內亦有廠商在S4A的系統之上開發出 Motoduino 的專案( [http://www.motoduino.com/](http://www.motoduino.com/) )。

## 韌體下載

可以直接從 S4A 的官網下載。

download : [http://vps34736.ovh.net/S4A/S4AFirmware16.ino](http://vps34736.ovh.net/S4A/S4AFirmware16.ino)  

S4A 韌體名稱: S4AFirmware16.ino

這個是一個 Arduino 的 .ino 檔，所以直接用 Arduino 的 IDE 打開之後就可以上傳到板子上了。

## 圖形化程式語言下載

去 S4A 官網就可以看到針對三大平台(Windows, MacOSX, Linux-Debian)的安裝程式。

[http://s4a.cat/](http://s4a.cat/)


## 連線 通訊協定

S4A 通過 UART 介面來和圖形化程式語言溝通。而其中的通訊協定很簡單，從官網提供的資料如下:

[http://s4a.cat/downloads/s4a-protocol.pdf](http://s4a.cat/downloads/s4a-protocol.pdf)


UART 連線預設設定為 38400 8-N-1 (motorduino 的設定據說是 57600 bps)。帶有 S4A 韌體的 Arduino 會一直透過 UART 發送 2 byte 為一組的封包。封包結構分為 high_byte 和 low_byte。每組封包帶有下面兩個資訊:

- Channel Number : 0~15 (4bit)
- Channel Data   : 0~1023 (10bit)

所以兩個 byte 為一組的封包結構如下:
    
          high_byte          low_byte
    [ H C C C C X X X ] [ L X X X X X X X ]
      7 6 5 4 3 2 1 0     7 6 5 4 3 2 1 0 
      
    high_byte :
        [7] == 1
        [6:3] == Channel number [3:0]
        [2:0] == Channel Data [9:7]
        
    low_byte : 
        [7] == 0
        [6:0] == Channel Data [6:0]

Channel Number 數值對應的裝置要分成兩張表來看，一張是由S4A程式言語(電腦)傳給S4A韌體(Arduino)如下:

    4: (D4) Continuous rotation Servomotor: 0="motor off", 1="clockwise", 2="anticlockwise"
    5: (D5) PWM output: 0 ~ 255
    6: (D6) PWM output: 0 ~ 255
    7: (D7) Continuous rotation Servomotor: 0="motor off", 1="clockwise", 2="anticlockwise"
    8: (D8) Servo motor (Angle control) : 0 ~ 360
    9: (D9) PWM output : 0 ~ 255
    10: (D10) Digital Output : 0/1
    11: (D11) Digital Output : 0/1
    12: (D12) Servo motor (Angle control) : 0 ~ 360
    13: (D13) Digital Output : 0/1

可以看到每個號碼所對應的都是輸出裝置(output)。所以另一張由S4A韌體(Arduino)傳給S4A程式語言的部份，是以感測器為主。

    0: (A0) Analog input : 0 ~ 1023
    1: (A1) Analog input : 0 ~ 1023
    2: (A2) Analog input : 0 ~ 1023
    3: (A3) Analog input : 0 ~ 1023
    4: (A4) Analog input : 0 ~ 1023
    5: (A5) Analog input : 0 ~ 1023
    6: (D2) Digital input : 0/1
    7: (D3) Digital input : 0/1


Arduino部份會每 16ms 傳送一次給電腦，每次都會 8 組封包( Channel Number: 0~7)共 16 byte 。  


而電腦則是每 80 ms 傳送一次給 Arudino，每次都會送 10 組封包( Channel Number: 4~13) 共 20 byte 。
	