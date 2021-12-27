# -*- coding: utf-8 -*-
# Written by Birch - Sindragosa

import gspread
import os
import re
from datetime import datetime


config = open('config.txt', 'r').read().split('\n')
path = re.findall(r"\"(.*)\"", config[1])[0]
sheets_id = re.findall(r"\"(.*)\"", config[2])[0]
sheet_name = re.findall(r"\"(.*)\"", config[3])[0]
sheets = False


if os.path.exists(path):
    if len(sheets_id) > 0:
        sheets = True 
        gc = gspread.service_account(filename='credentials.json')
        sh = gc.open('lootcrawler').sheet1
        
        
    f = open(path, encoding="utf8")
    file = f.read().split('\n')

    rows = []
    for line in file:
        if '|Hchannel:OFFICER|h[Officer]|h' in line:
            msg = line.split(' ')
            date = msg[0]
            time = msg[1]
            if 'awarded' in msg:
                i = msg.index('awarded')
                player = msg[i-1]
                item = ' '.join(msg[i+1::])
                row = [date, time, player, item]
                rows.append([date, time, player, item])
    f.close()
    
    if sheets:
        sh.append_rows(rows)
    
    
    now = datetime.now()
    current_time = now.strftime("%D%H%M%S").replace('/', '')
    
    saveString = "Log/Lootcrawler {0}.txt".format(current_time)
    f = open(saveString,"a")
    for row in rows:
        f.write(' '.join(row))
        f.write('\n')
    f.close()
    
    
if os.path.exists(path):
    os.remove(path)