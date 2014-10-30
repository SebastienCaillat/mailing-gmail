#!python3
# -*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
success=failure=0
# ------ username and password in gmail --------
# ------ nom d'utilisateur et mot de passe dans gmail --------
uname='your.username@gmail.com'
passwd = 'password'
# ----------- Ici le sujet / message title ----------- 
Subject="Here message subject"
# ------------ Le texte du mél / message ----------------
Text="""Here,
your message
"""
# ------ les destinataires / to  ----
# ------ remove & replace # enlever et remetre les # ------- 
To=['adresse1@nimportequoi.com']
#To=['adresse2@nimportequoi.com','adresse3@nimportequoi.com']
total=len(To)
# --------- Message / Assemblage du message ------------
From='your.username@gmail.com'
message = MIMEText(Text, _charset='ISO-8859-1')
message['Subject'] = Header(Subject, 'utf-8')
message.add_header('reply-to', 'your.username@gmail.com')
# ---------- Connexion gmail ----------------
print ('Message title:',Subject)
print ('Number of messages to send:',total)
print ('Trying to connect to:',uname)
s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
try:
    connect = s.login(uname, passwd)
    print (connect)
    for to in To:
        try:
            send = s.sendmail(From, to, message.as_string())
            print ('Message sent to: '+to)
            success+=1
        except:
            print ('Error sending message to: '+to)
            failure+=1
finally:
    disconnect=s.quit()
    print ('Disconnecting')
    print (disconnect)
    print ('Messages send success:',success,', failure(s):', failure)
