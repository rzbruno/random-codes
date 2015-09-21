#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib

gmail_user = ""
gmail_pwd = ""
FROM = ''
TO = ['']
SUBJECT = ""
TEXT = ""

message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
   server = smtplib.SMTP("smtp.gmail.com", 587)
   server.ehlo()
   server.starttls()
   server.login(gmail_user, gmail_pwd)
   server.sendmail(FROM, TO, message)
   server.close()
   print('successfully sent the mail')
except:
   print("failed to send mail")
