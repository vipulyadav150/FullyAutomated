#Python Script to check for Daily Messages(Current Date)

import datetime , imapclient , pyzmail ,pprint , imaplib


acc_addr = input('Enter Your Email Address : ')
acc_pass = input('Enter your Email Password : ')
date_today = str(datetime.date.today())
today_date = date_today[8] + date_today[9]
today_month = date_today[5] + date_today[6]
if today_month == '04':
    month_use = 'Apr'
#print(type(today_month))
#print(today_date)
#print(today_month)
current_year = date_today[0:4]
#print(current_year)

#net_set_date = month_use + ' ' + today_date +  ',' + current_year
net_set_date =  today_date + '-' + 'Apr' + '-' + current_year

print(net_set_date)
string_key = 'ON' + ' ' + net_set_date



imapO = imapclient.IMAPClient('imap.gmail.com', ssl = True)
imapO.login(acc_addr , acc_pass)
imapO.select_folder('INBOX')
UIDs_current = imapO.search(string_key)
raw_msg = imapO.fetch(UIDs_current , ['BODY[]'])
print('All Your Mails for today ' + net_set_date + ':' )
for id in UIDs_current:
    msg = pyzmail.PyzMessage.factory(raw_msg[id][b'BODY[]'])
    print(msg.get_subject())
    print(msg.get_addresses('to'))
    print(msg.get_addresses('from'))
    print(msg.get_addresses('cc'))
    print(msg.get_addresses('bcc'))
    if msg.text_part != None:
        msg_cont = msg.text_part.get_payload().decode(msg.text_part.charset)
        print(msg_cont)