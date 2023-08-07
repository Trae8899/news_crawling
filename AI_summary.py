import openai
from get_api import api
import json

prompt_summary = '''You are an expert at summarizing
when I let you know the URL 
Then say the title and summarize what the URL provides
And the summary is from 3 to 5 sentences so that i will not refer to the original.
and don't tell me the check the original url
and result should be a korean and json type data
"Title_Kr":{title},"Summary_Kr":{summary}'''

import openai
openai_api=api("OPENAI")
client_id = openai_api['ID']
openai.api_key = openai_api['KEY']

def Article_En_Summary2Kr(url):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You're an expert at summarizing\nI give you the URL, you give me the title, and you summarize the article.\n\nKeep the summary to 3-5 sentences so I don't have to see the original article, and don't tell me to check the original URL.\n\nAnd when I create a YouTube short video with the title and summary, tell me specifically how many views you expect.\n\nThe title and summary must be in korean and JSON type\n\n\"Title_Kr\":{title}, \"Summary_Kr\":{summary}, \"Views\":{Expected Views}"
        },
        {
        "role": "user",
        "content": "https://www.reuters.com/technology/paypal-launches-stablecoin-crypto-push-2023-08-07/"
        },
        {
        "role": "assistant",
        "content": "\"Title_Kr\": \"페이팔, 스테이블코인을 출시하여 암호화폐 시장 진출\",\n\"Summary_Kr\": \"페이팔은 2023년에 암호화폐 시장에 진출하기 위해 스테이블코인을 출시할 계획이다. 스테이블코인은 가치가 변동하지 않는 암호화폐로, 페이팔은 이를 통해 안정적인 결제 수단을 제공하고자 한다. 이러한 동향은 암호화폐 시장의 성장과 함께 전 세계적으로 디지털 결제 수단의 수요가 증가하고 있는 것을 반영한다.\",\n\"Views\": 8532"
        },
        {
        "role": "user",
        "content": url
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=0.3,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response['choices'][0]['message']['content']

def Article2json(url):
    cont=Article_En_Summary2Kr(url)
    # print (cont)
    fixed_str = cont.replace('""', '\"')

    # json_str = '{\"'+ Article_En_Summary2Kr(url).replace('""', '\",\"') + '\"}'
    json_str= '{' + fixed_str + '}'
    article=json.loads(json_str)
    # c=b['Title_Kr']
    # d=b["Summary_Kr"]
    return article