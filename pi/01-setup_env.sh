#!/bin/sh

echo "Add ftp.yzu.edu.tw site into apt source.list"
sed -i "1ideb ftp://ftp.yzu.edu.tw/Linux/raspbian/raspbian/ jessie main contrib non-free rpi" /etc/apt/sources.list
apt-get update
