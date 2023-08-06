import newspy
import json

# 임포트한 CNBC와 WSJ 라이브러리에서 CNBC_POP 및 WSJ_popular 함수를 구현합니다.
from NEWS_Source.Thebell import Thebell
from datetime import datetime

today = datetime.today().strftime('%y-%m-%d')

def News_Json():

    gisa = []

    #Thebell
    try:
        thebell=Thebell()
        for bell in thebell:
            try:
                gisa.append([bell[0],newspy.news(bell[0],"ko")])
            except:
                continue
    except:
        pass

    news = []

    i=0
    for gisat in gisa:
        i=i+1
        arlink = gisat[0]
        artitle = gisat[1][0]
        artext = gisat[1][1]
        arsumy = artext
        koartitle = artitle
        koarsumy = arsumy

        news.append({'Language':'Kr','No':i,'Date': today, 'Link': arlink, 'Title': artitle, 'Text': artext,
                        'Summary': arsumy, 'Title_Kr': koartitle, 'Summary_Kr': koarsumy})

    return news