#!/usr/bin/env python
import sys
import time
import paramiko 
import os
import cmd
import datetime
import socket

#authentication
#ip='10.10.10.10'
#USER = 'garkushaaa'
#PASSWORD = ''
#USER = 'atostest'
#PASSWORD = ''
print "enter username"
USER = raw_input()
print "enter password"
PASSWORD = raw_input()
port = 22
str1='dot1x-user'
str2='dot1x-printer'
commandint='no authentication port-control auto'
#commandint1='authentication order mab dot1x'
#commandint2='end'
commandint3='do write mem'



fip = open('ip_allianze.txt','rU')
for lineip in fip.readlines():
    ip=lineip.replace('\n','')
    print (lineip)
    
    f1='res_out_'+ ip+'.txt'
    f2='res_in_'+ ip+'.txt'
    wr = open(f1,'w')
    wr1 = open(f2,'wb')



    #ssh session starts
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=ip, username=USER, password=PASSWORD,port=port,timeout=5)
        stdin, stdout, stderr = client.exec_command("show inter desc")
        time.sleep(1)
        rez=stdout.read()
        wr1.write(rez)
        client.close()
    except paramiko.ssh_exception.SSHException:
        print ("ssh e fail host=",ip,"\n")
    except paramiko.ssh_exception.NoValidConnectionsError:
        print ("no valid fail host=",ip,"\n")
#   except paramiko.ssh_exception.TimeoutError:
#        print ("fail host=",ip,"\n")
    except (paramiko.SSHException, socket.error, socket.timeout):
	 print ("timeout fail host=",ip,"\n")
    wr1.close()
    f = open(f2,'rU')


    wr.write ('conf t'+ '\n')
    wr.write ('!'+ '\n')
    for line in f.readlines():
        #str=f.readline()
        #print(line)
        if line.find(str1) != -1 or line.find(str2) != -1:
            print(line)
#            print('============')
            int1=line.split(" ",1)
#            print(int1[0])
            wr.write ('interface '+ str(int1[0]) + '\n')
            wr.write (commandint + '\n')
           # wr.write (commandint1 + '\n')
           # wr.write (commandint2 + '\n')
           # wr.write (commandint3 + '\n')
            wr.write ('!'+ '\n')
        #if line.find(str2) != -1 :
         #   print(line)
          #  print('============')
           # int2=line.split(" ",1)
            #print(int2[0])
            #wr.write ('interface '+ str(int2[0]) + '\n')
            #wr.write (commandint + '\n')
            #wr.write ('!'+ '\n')
       
   # wr.write (commandint2 + '\n')
    wr.write (commandint3 + '\n')
    
   
        #time.sleep(2)
    f.close()
    wr.close()

    # dobavlenie v konfig
    f = open(f1,'rU')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try: 
    	client.connect(hostname=ip, username=USER, password=PASSWORD,port=port,timeout=5)
    	chan = client.invoke_shell()
        
    	for line in f.readlines():
        	time.sleep(1)
        	chan.send(line)
    	print (ip+'config applied')
	client.close()
    except paramiko.ssh_exception.SSHException:
        print ('fail host='+ip+'\n')
    except paramiko.ssh_exception.NoValidConnectionsError:
        print ("fail host=",ip,"\n")
#   except paramiko.ssh_exception.TimeoutError:
#        print ("fail host=",ip,"\n")
    except (paramiko.SSHException, socket.error,socket.timeout):
         print ("fail host="+ip+'\n')

    f.close()

fip.close()

