#!/bin/sh

echo "------------------------------"
echo "install python3 Dev tools"
echo "------------------------------"
apt-get install -y ipython3-notebook python3-dev python3-pip geany geany-plugin-py bpython3


echo "---------------------------------"
echo "install python3 i2c, spi, flask  "
echo "---------------------------------"
apt-get install -y python3-smbus python3-spidev python3-flask


echo "----------------------------------"
echo " pip install python class packages"
echo "----------------------------------"
#pip install numpy scipy sympy pandas requests lxml

#apt-get install liblxml2-dev libxslt1-dev
#pip3 install lxml

#apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran
#pip install scipy

#apt-get install python3-numpy python3-scipy python3-matplotlib python3-pandas python3-pandas-lib python3-lxml python3-requests 
#pip install sympy

