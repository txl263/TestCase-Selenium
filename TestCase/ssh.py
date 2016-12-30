#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# filename: pexpect_test.py  
import pexpect  
      
if __name__ == '__main__':  
    user = 'root'  
    ip = '10.40.45.97'  
    child = pexpect.spawn('ssh %s@%s' % (user,ip))
    child.expect ('password:')  
    child.sendline (mypassword)  
    child.expect('#')  
    child.sendline('./qpython-android5.sh sms.py')  
    child.expect('#')  
    
    sql =  child.before   # Print the result of the ls command.  
    child.sendline('exit')
    # child.interact()     # Give control of the child to the user.  
    print sql
    pass  
