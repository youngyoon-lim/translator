import html
import translators as ts
import requests
from bs4 import BeautifulSoup
import os
from google.cloud import translate_v2 as translate
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r"/workspace/google_translate/GoogleCloudKey.json"
client = translate.Client()


html = '''
<html>
<head>
<title>That is the display section.</title>
</head>
<body>
<p>So got the stairs.</p>
<p>Yes, said Arthur, yes I did. It was displayed at the bottom of the locked filing cabinet stuck in a dormant toilet with a sign on the door saying 'Be wary of the leopard'</p></body>
</html>
'''

# target = "ko"

# url = 'https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/'
# res = requests.get(url)
# html2 = res.content
soup = BeautifulSoup(html, 'html.parser')
print(soup)


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


elements = ['p','title']
# print(soup.findAll(soup))

for i in soup.findAll(elements):
    i.string.replace_with(ts.google(i.string,from_language='en',    to_language='ko'))
print(soup)


