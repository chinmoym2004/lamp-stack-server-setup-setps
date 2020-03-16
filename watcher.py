#!/usr/bin/python3
#print("hello world")
import os,sys,time,datetime
hostname = sys.argv[1]
if hostname=='':
    print("HOST NAME not provided");
    exit(0);

print("Pinging Host : "+sys.argv[1]+"\n\n");
while 1:
    response = os.system("ping -c 1 "+hostname)
    if response==0:
        print(datetime.datetime.now()+" :  Server is UP\n\n")
    else:
        print(datetime.datetime.now()+" ; Server is DOWN !!!!\n\n")
    time.sleep(120)

