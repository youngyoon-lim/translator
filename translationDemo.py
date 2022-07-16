import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/workspace/google_translate/GoogleCloudKey.json"
client = translate.Client()


f = open('/workspace/google_translate/en_text.txt', 'r')
text = f.read()


target = "ko"

output = client.translate(text, target_language=target)

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
print(sorted_output[2][1])

