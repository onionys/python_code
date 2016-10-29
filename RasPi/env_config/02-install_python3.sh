#!/bin/sh

echo "------------------------------"
echo "install python3 Dev tools"
echo "------------------------------"
apt-get install -y python3-dev python3-pip


echo "---------------------------------"
echo "install python3 i2c, spi         "
echo "---------------------------------"
apt-get install -y python3-smbus python3-spidev


echo "----------------------------------"
echo " pip install python class packages"
echo "----------------------------------"
#pip install numpy scipy sympy pandas requests lxml

apt-get install -y libxml2-dev libxslt-dev
pip3 install lxml requests
pip3 install "ipython[all]"



#apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran
#pip install scipy

#apt-get install python3-numpy python3-scipy python3-matplotlib python3-pandas python3-pandas-lib python3-lxml python3-requests 
#pip install sympy

