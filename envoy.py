# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 22:04:27 2025

@author: PC
"""

import smtplib
from email.mine.text import MINEText
sujet="bonjour"
corps="saidoujonathan65@gmail.com"
mot_de_passe="sa65jo"
message=MINEText(corps)
message['Subject']=sujet
message['From']="alysawadogo001@gmail.com"
message['To']="saidoujonathan65@gmail.com"
try:
    with smtplib.SMTP_SSL('smtp.gmail.com,465'):
        server.login("alysawadogo001@gmail.com",sa65jo)
        server.sendmail("alysawadogo001@gmail.com", "saidoujonathan65@gmail.com",message_as_string())