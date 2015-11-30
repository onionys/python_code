## LCM.py module

### ex code
    from LCM import qc1602a
    lcd = qc1602a()

    lcd.move(1,1)
    lcd.write_msg("Hello")

    lcd.move(2,1)
    lcd.write_msg("World")
    

可將LCM.py檔案複製到 /home/pi/ 底下，並修改 /etc/rc.local 檔案。

將 "python3 /home/pi/LCM.py &" 插入檔案的 "exit 0" 的上一行位址:(如下)

    .....
    _IP=$(hostname -I) || true
    if [ "$_IP" ]; then
      printf "My IP address is %s\n" "$_IP"
    fi
    python3 /home/pi/LCM.py &              # <<----加入這一行
    exit 0 



這樣Raspberry Pi 在開機就會去執行LCM.py並在LCM模組上顯示出IP位址。    
可以試著加入程式碼，增加 "使用按鈕停止 LCM.py 埶行" 的功能。

# 其他Python相關資料

## IPython 使用

IPython notebook 使用教學(簡體中文)
[http://mindonmind.github.io/2013/02/08/ipython-notebook-interactive-computing-new-era/](http://mindonmind.github.io/2013/02/08/ipython-notebook-interactive-computing-new-era/)


IPython Magics 介紹(英文)
[http://nbviewer.ipython.org/github/ipython/ipython/blob/1.x/examples/notebooks/Cell%20Magics.ipynb](http://nbviewer.ipython.org/github/ipython/ipython/blob/1.x/examples/notebooks/Cell%20Magics.ipynb)


IPython Cookbook (英文)
[https://github.com/ipython/ipython/wiki/Cookbook%3A-Index](https://github.com/ipython/ipython/wiki/Cookbook%3A-Index)


IPython Tips & Tricks (English)
[https://ipython.org/ipython-doc/2/interactive/tips.html#tips](https://ipython.org/ipython-doc/2/interactive/tips.html#tips)
