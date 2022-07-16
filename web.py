import html
import translators as ts
import requests
from bs4 import BeautifulSoup
import os
import sys
from google.cloud import translate_v2 as translate
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/workspace/google_translate/GoogleCloudKey.json"
client = translate.Client()


# html = '''
# <html>
# <head>
# <title>That is the display section.</title>
# </head>
# <body>
# <p>So got the stairs.</p>
# <p>Yes, said Arthur, yes I did. It was displayed at the bottom of the locked filing cabinet stuck in a dormant toilet with a sign on the door saying 'Be wary of the leopard'</p></body>
# </html>
# '''


target = "ko"

url = 'http://www.ditext.com/sellars/epm1.html'
res = requests.get(url)
html = res.content
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# sys.stdout = open('output.txt','w')


# blacklist = [
#     '[document]',
#     'noscript',
#     'header',
#     'html',
#     'meta',
#     'head', 
#     'input',
#     'script',
#     'style',
#     'li',
#     'div',
#     'a'
#     # there may be more elements you don't want, such as "style", etc.
# ]


elements = ['p','title','i','h3']
# print(soup.findAll(soup))

for i in soup.findAll(elements):
    print("read_string = " , i.string)
    target_sentence = ts.google(ts.google(str(i.string),from_language='en', to_language='ko'))
    print("target_sentece = ", target_sentence)
    # i.string.replace_with(target_sentence)
    # i.string(target_sentence)
print(soup)


