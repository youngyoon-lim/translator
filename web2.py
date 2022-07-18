import html
import translators as ts
import requests
from bs4 import BeautifulSoup
import os
from google.cloud import translate_v2 as translate
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/workspace/web_translator/GoogleCloudKey.json"
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

target = "ko"

# url = 'https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/'
# res = requests.get(url)
# html2 = res.content

soup = BeautifulSoup(html, 'html.parser')
print(soup)


elements = ['p','title']
# print(soup.findAll(soup))

for i in soup.findAll(elements):
    output = client.translate(str(i), target_language=target)
    #output type 확인
    '''
    print(type(output))
    print(output)
    '''

    # dic -> Tuple pair로 이루어진 List로 리턴
    sorted_output = sorted(output.items())
    '''
    print(sorted_output)
    print(type(sorted_output))
    '''
    print(sorted_output[2][1].replace("&#39;", "'"))

    
# for i in soup.findAll(elements):
#     i.string.replace_with(ts.google(i.string,from_language='en',to_language='ko'))
# print(soup)


