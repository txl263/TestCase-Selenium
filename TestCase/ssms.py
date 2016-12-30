# -*- coding: utf-8 -*-
import paramiko
from scp import SCPClient
import sqlite3
import datetime
import time

Host = '10.40.45.97'
user = "root"
passwd = "xxxxxxx"
port = 22
paramiko.util.log_to_file("filename.log")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #允许连接不在know_hosts文件中的主机。
print Host,port,user,passwd

ssh.connect(Host,port,user,passwd)
ssh.connect('10.40.45.97',port,'root','xxxxxxx',)
scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
remotepath='/data/data/com.android.providers.telephony/databases/mmssms.db'
# localpath='/data/data/com.android.providers.telephony/databases/mmssms.db'
# scpclient.put(localpath, remotepath)  # 上传到服务器指定文件
localpath1 = 'mmssms.db'
scpclient.get(remotepath, localpath1)  #从服务器中获取文件
ssh.close()

cx = sqlite3.connect("mmssms.db")
cursor = cx.execute("SELECT date,address,body FROM sms where address='106575008296' order by date desc limit 1")
cx.fetchall()

print datetime.datetime.now()




