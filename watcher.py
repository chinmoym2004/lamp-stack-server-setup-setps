#!/usr/bin/python3
#print("hello world")
import os,sys,time,datetime

if len(sys.argv) < 3:
   print('You need to pass HOSTNAME and PING INTERVAL')
   sys.exit()

hostname = sys.argv[1]
if hostname=='':
    print("HOST NAME not provided");
    sys.exit(0)

Ptime = sys.argv[2]
if Ptime=='':
    print("Specify a ping interval");

print("Pinging Host : "+sys.argv[1]+", Ping interval "+Ptime+"\n\n");
while 1:
    response = os.system("ping -c 1 "+hostname)
    if response==0:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" :  Server is UP\n\n")
    else:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" ; Server is DOWN !!!!\n\n")
    time.sleep(int(Ptime))

