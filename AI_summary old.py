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
        "content": "You are an expert at summarizing\nwhen I let you know the URL \nThen say the title and summarize what the URL provides\nAnd the summary is from 3 to 5 sentences so that i will not refer to the original.\nand don't tell me the check the original url\nand result should be a korean and json type data\n\"Title_Kr\":{title},\"Summary_Kr\":{summary}"
        },
        {
        "role": "user",
        "content": "https://www.reuters.com/markets/us/jpmorgan-raises-us-economic-growth-estimate-no-longer-expects-2023-recession-2023-08-04/"
        },
        {
        "role": "assistant",
        "content": "\"Title_Kr\": \"JP모건, 미국 경제 성장 예상치 상향 조정, 2023년 경기침체 예상 취소\",\n\"Summary_Kr\": \"JP모건은 미국 경제 성장 예상치를 상향 조정했으며, 2023년 경기침체가 예상되지 않는다고 밝혔다. 이는 미국 경제의 회복세가 예상보다 강력하다는 것을 의미한다. JP모건은 이러한 상황에 따라 미국 연방준비제도(Fed)가 금리 인상을 더욱 빠르게 추진할 수 있다고 전망하고 있다.\""
        },
        {
        "role": "user",
        "content": url
        }
    ],
    temperature=0.3,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response['choices'][0]['message']['content']

def Article2json(url):
    json_answer= "{" + Article_En_Summary2Kr(url) + "}"
    article=json.loads(json_answer)
    # c=b['Title_Kr']
    # d=b["Summary_Kr"]
    return article

def multiarticle(urls):
    json_answer= Article_En_Summary2Kr(urls)
    article=json.loads(json_answer)
    for item in article:
        print("Title: ", item["Title_Kr"])
        print("Summary: ", item["Summary_Kr"])
        print("----------------------")
    

# a=Article2json('''https://www.reuters.com/markets/us/fitch-us-downgrade-followed-protocols-despite-timing-questions-2023-08-04/
# https://www.reuters.com/markets/argentina-agrees-775-mln-loan-with-qatar-make-imf-repayment-2023-08-04/
# https://www.reuters.com/markets/us/us-businesses-hoarding-workers-even-economy-cools-2023-08-04/
# https://www.reuters.com/business/finance/carl-icahns-investment-firm-cuts-dividend-months-after-hindenburg-report-2023-08-04/''')
# c=a['Title_Kr']
# d=a["Summary_Kr"]
# print (a)
# print (c)
# print (d)

# import json

# data = '[\n  {\n    "Title_Kr": "피치, 미국의 강등은 타이밍 문제에도 불구하고 프로토콜을 따랐다",\n    "Summary_Kr": "피치는 미국의 신용등급 강등이 타이밍 문제에 대한 의문을 제기하지만 프로토콜을 따랐다고 밝혔다. 이는 피치가 신용등급 평가를 수행할 때 일정한 절차와 기준을 준수했다는 것을 의미한다. 미국의 신용등급 강등은 경제에 대한 우려와 관련이 있으며, 이에 대한 피치의 결정은 신뢰성을 유지하기 위해 중요한 역할을 한다."\n  },\n  {\n    "Title_Kr": "아르헨티나, 카타르와 7.75억 달러 대출 합의로 IMF 상환 가능",\n    "Summary_Kr": "아르헨티나는 카타르와 7.75억 달러 대출 합의를 이루어 IMF 상환을 가능하게 했다. 이는 아르헨티나가 IMF에 대한 빚을 상환하기 위해 외부 자금을 확보한 것을 의미한다. 아르헨티나는 경제적 어려움을 겪고 있으며, 이번 합의는 경제 안정을 위한 긍정적인 발전이다."\n  },\n  {\n    "Title_Kr": "미국 기업들, 경기가 둔화되더라도 종업원을 보유 중",\n    "Summary_Kr": "미국 기업들은 경기가 둔화되더라도 종업원을 보유하고 있다. 이는 미국 경제의 불확실성에도 불구하고 기업들이 인력을 유지하려는 의지가 강하다는 것을 보여준다. 이러한 상황은 미국 경제의 회복세와 더불어 기업들의 신뢰도를 나타내는 지표로 볼 수 있다."\n  },\n  {\n    "Title_Kr": "칼 아이칸의 투자 회사, 힌덴버그 보고서 발표 몇 달 후 배당금을 삭감",\n    "Summary_Kr": "칼 아이칸의 투자 회사는 힌덴버그 보고서 발표 몇 달 후 배당금을 삭감했다. 이는 힌덴버그 보고서가 회사의 재무 건전성에 대한 의문을 제기하고, 이에 대한 대응으로 배당금을 조정한 것을 의미한다. 이러한 조치는 투자자들의 신뢰를 회복하기 위한 시도로 볼 수 있다."\n  }\n]'

# parsed_data = json.loads(data)

# for item in parsed_data:
#     print("Title: ", item["Title_Kr"])
#     print("Summary: ", item["Summary_Kr"])
#     print("----------------------")