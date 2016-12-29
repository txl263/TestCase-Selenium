# -*- coding: utf-8 -*-
import paramiko
import password
from scp import SCPClient
 
Host = '10.40.45.97'
user = "root"
passwd = "781025"
port = 22
paramiko.util.log_to_file("filename.log")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #允许连接不在know_hosts文件中的主机。
print Host,port,user,passwd

ssh.connect(Host,port,user,passwd)
ssh.connect('10.40.45.97',port,'root','781025',)
# t = paramiko.Transport(("10.40.45.97","22"))

 
scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
remotepath='/data/data/com.android.providers.telephony/databases/mmssms.db'
localpath='/data/data/com.android.providers.telephony/databases/mmssms.db'
# scpclient.put(localpath, remotepath)  # 上传到服务器指定文件
localpath1 = 'mmssms.db'
scpclient.get(remotepath, localpath1)  #从服务器中获取文件
ssh.close()


# remote_file = "/data/data/com.android.providers.telephony/databases/mmssms.db"
# local_file = " C:\Users\Eric\Documents\GitHub\TestCase-Selenium\TestCase\mmssms.db"
# ssh_scp_get('10.40.45.97',22,user,password,remote_file,local_file)



