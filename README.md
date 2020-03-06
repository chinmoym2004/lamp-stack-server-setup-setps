# lamp-stack-server-setup-setps
Quick lines of code that can help to setup LAMP stack

To run the file , you need to add execution permission (if you don't see its there).
1. `run  sudo ./server-setup.sh`
2. mysql_secure_installation to set password policy and secure user 
3. To create new user in mysql
  `CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';`
 `GRANT ALL PRIVILEGES ON * . * TO 'username'@'localhost';`
 `FLUSH PRIVILEGES;`
