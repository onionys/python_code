#!/bin/sh

echo "Add ftp.yzu.edu.tw site into apt source.list"
sed -i "1ideb ftp://ftp.yzu.edu.tw/Linux/raspbian/raspbian/ jessie main contrib non-free rpi" /etc/apt/sources.list
apt-get update
rm /usr/bin/python
ln -s /usr/bin/python3 /usr/bin/python


echo "------------------------------"
echo "install chinese font and input"
echo "------------------------------"
apt-get install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy scim scim-tables-zh scim-chewing
