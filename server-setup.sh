#!/bin/
# installation of php 7.2 mysql apache2 in Debian/Ubuntu server - 18.04 server 
sudo apt install apache2 php7.2 mysql-server php7.2-mbstring php7.2-curl php7.2-zip php7.2-xml php7.2-gd php7.2-intl php7.2-mysql

# -- run mysql_secure_installation to set password policy and secure user 
# -- TO CREATE NEW MYSQL USER
#CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
#GRANT ALL PRIVILEGES ON * . * TO 'username'@'localhost';
#FLUSH PRIVILEGES;