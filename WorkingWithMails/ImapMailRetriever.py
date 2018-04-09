import imapclient , pyzmail , pprint


imapObj = imapclient.IMAPClient('imap.gmail.com',ssl='True')
imapObj.login('vipulyadav150@gmail.com','VipulYad@v150')
imapObj.select_folder('INBOX',readonly=True)
UIDsList = imapObj.search(['UNSEEN'])
UIDsList_Intern = imapObj.gmail_search('Internshala')

#print(UIDsList)
#print(UIDsList_Intern)
#pprint.pprint(imapObj.list_folders())
rawMessages = imapObj.fetch(UIDsList_Intern , ['BODY[]'])
#pprint.pprint(rawMessages)


message = pyzmail.PyzMessage.factory(rawMessages[4565][b'BODY[]'])
msg_subject = message.get_subject()
msg_from = message.get_addresses('from')
msg_to = message.get_addresses('to')
msg_cc = message.get_addresses('cc')
msg_bcc = message.get_addresses('bcc')
print(msg_subject)
print(msg_from)
print(msg_to)
print(msg_cc)
print(msg_bcc)

if message.text_part != None:
    message_main = message.text_part.get_payload().decode(message.text_part.charset)
    print(message_main)

imapObj.logout()






