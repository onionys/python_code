
sudo mkdir /usr/lib/jvm
sudo mv ./jdk1.7* /usr/lib/jvm/jdk1.7.0
sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.7.0/bin/java" 1
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.7.0/bin/javac" 1
sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jvm/jdk1.7.0/bin/javaws" 1
sudo chmod a+x /usr/bin/java
sudo chmod a+x /usr/bin/javac
sudo chmod a+x /usr/bin/javaws

# edit .bashrc
# JAVA_HOME=/usr/lib/jvm/jdk1.7.0
# PATH=$PATH:$HOME/bin:$JAVA_HOME/bin
