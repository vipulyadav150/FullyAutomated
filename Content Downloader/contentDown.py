import requests



res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(len(res.text))
storeFile = open('storeContent.txt','wb')
#print(res.text)
for text in res.iter_content(len(res.text)):
    storeFile.write(text)
storeFile.close()
