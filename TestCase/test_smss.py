#!/usr/bin/env python
#-*- coding:utf-8 -*-
#qpy:console
import sqlite3
import datetime
import time


cx = sqlite3.connect("/data/data/com.android.providers.telephony/databases/mmssms.db")
cursor = cx.execute("SELECT date,address,body FROM sms where address='106575008296' order by date desc limit 1")
result=cursor.fetchall()
print result

cursor.close
cx.close
