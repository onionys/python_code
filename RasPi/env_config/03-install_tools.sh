#!/bin/sh

echo "------------------------------"
echo "install common tools"
echo "------------------------------"
apt-get install -y vim vim-nox ctags automake subversion  gedit
# apt-get install vim-python-jedi python3-jedi
# vim-addons status
# vim-addons install python-jedi

echo "-------------------------------"
echo "install chinese fonts and input"
echo "-------------------------------"
apt-get install -y ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy scim scim-tables-zh scim-chewing

