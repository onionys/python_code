#!/bin/sh

echo "------------------------------"
echo "install common tools"
echo "------------------------------"
apt-get install vim ctags automake subversion  gedit

echo "------------------------------"
echo "install python3 Dev tools"
echo "------------------------------"
apt-get install ipython3-notebook python3-dev python3-pip geany geany-plugin-py bpython3

echo "---------------------------------"
echo "install python3 i2c, spi, flask  "
echo "---------------------------------"
apt-get install python3-smbus python3-spidev python3-flask

echo "------------------------------"
echo "install chinese font and input"
echo "------------------------------"
apt-get install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy scim scim-tables-zh scim-chewing


