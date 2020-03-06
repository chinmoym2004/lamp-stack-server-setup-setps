# lamp-stack-server-setup-setps
Quick lines of code that can help to setup LAMP stack

To run the file , you need to add execution permission (if you don't see its there).
1. `run  sudo ./server-setup.sh`
2. mysql_secure_installation to set password policy and secure user 
3. CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';\n
GRANT ALL PRIVILEGES ON * . * TO 'username'@'localhost';\n
FLUSH PRIVILEGES;
