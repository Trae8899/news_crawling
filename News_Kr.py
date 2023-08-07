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
                gisa.append(bell[0])
            except:
                continue
    except:
        pass

    news = []

    i=0
    for gisat in gisa:
        try:
            i=i+1
            arlink = gisat
            artitle = newspy.news(arlink,"ko")[0]
            artext = ""
            arsumy = artext
            koartitle = artitle
            koarsumy = arsumy
            hits=100-i
            news.append({'Language':'Kr','Date': today, 'Link': arlink, 'Title': artitle, 'Title_Kr': koartitle, 'Summary_Kr': koarsumy,'Hits':hits})
        except Exception as e:
            print (e)
            continue
    news.sort(key=lambda x: x['Hits'], reverse=True)


    return news