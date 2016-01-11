#!/bin/sh

echo "------------------------------"
echo "install common tools"
echo "------------------------------"
apt-get install -y vim ctags automake subversion  gedit

echo "-------------------------------"
echo "install chinese fonts and input"
echo "-------------------------------"
apt-get install -y ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy scim scim-tables-zh scim-chewing

