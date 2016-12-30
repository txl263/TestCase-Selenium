# -*- coding: utf-8 -*-
import paramiko
from scp import SCPClient
import sqlite3
import datetime
import time
import pexpect 

# import ssh

Host = '10.40.45.97'
user = "root"
passwd = "xxxxxx"
port = 22
paramiko.util.log_to_file("filename.log")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #允许连接不在know_hosts文件中的主机。
print Host,port,user,passwd
# ssh.connect(Host,port,user,passwd)
# ssh.connect('10.40.45.97',port,'root','781025',)

# 新建一个ssh客户端对象
myclient = paramiko.SSHClient()
# 设置成默认自动接受密钥
myclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程主机
myclient.connect('10.40.45.97',port,'root','781025',)
stdin, stdout, stderr = myclient.exec_command("./qpython-android5.sh sms.py")

print stdout.read() 