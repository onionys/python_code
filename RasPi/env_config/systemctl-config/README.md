# systemctl 

## *.service file
    pathname: /lib/systemd/system/*.service
    example code:

    -- mqtt-msg-receiver.service
    [Unit]
    Description=mqtt lora msg logger 
    After=network.target rc.local.service
    
    [Service]
    Type=idle
    ExecStart=/usr/bin/python3 /home/onionys/code/mqtt-data-base/mqtt-data-recv.py > /home/onionys/code/mqtt-data-base/database/syslog 2>&1
    --
    
## command
    > sudo systemctl daemon-reload
    > sudo systemctl enable mqtt-msg-receiver.service
    then reboot....
