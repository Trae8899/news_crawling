import newspy
import json

# 임포트한 CNBC와 WSJ 라이브러리에서 CNBC_POP 및 WSJ_popular 함수를 구현합니다.
from NEWS_Source.CNBC import CNBC_POP
from NEWS_Source.WSJ import WSJ_popular
from NEWS_Source.cnnfinance import Cnn_pop
from NEWS_Source.reuters import Reuters_pop
from NEWS_Source.marketwatch import Marketwatch_POP
from NEWS_Source.investing import Investing_POP
import do_summary
from datetime import datetime
import AI_summary

today = datetime.today().strftime('%y-%m-%d')
def News_Json():
    
    gisa = []
    #Investing
    
    try:
        Iv_hot = Investing_POP()
        inv_no=0
        for investing in Iv_hot:
            if inv_no==5:
                break
            inv_no += 1
            try:
                gisa.append([investing[0],newspy.news(investing[0])])
            except:
                continue
    except:
        pass

    #Market Watch
    try:
        Mw_hot = Marketwatch_POP()
        for marketW in Mw_hot:
            try:
                gisa.append([marketW[0],newspy.news(marketW[0])])
            except:
                continue
    except:
        pass
    #CNBC
    try:
        cnbc_hot = CNBC_POP()
        for cnbc in cnbc_hot:
            try:
                gisa.append([cnbc[0],newspy.news(cnbc[0])])
            except:
                continue
    except:
        pass
    #Cnn
    try:
        cnn_hot = Cnn_pop()
        for cnn in cnn_hot:
            try:
                gisa.append([cnn[0],newspy.news(cnn[0])])
            except:
                continue
    except:
        pass
    #reuter
    try:
        reuters_hot = Reuters_pop()
        for reuter in reuters_hot:
            try:
                gisa.append([reuter[0],newspy.news(reuter[0])])
            except:
                continue
    except:
        pass
    # #WSJ
    # try:
    #     wsj_hot = WSJ_popular()
    #     for wsj in wsj_hot:
    #         try:
    #             gisa.append([wsj[0],newspy.news(wsj[0])])
    #         except:
    #             continue  
    # except:
    #     pass

    news = []

    i=0
    for gisat in gisa:
        try:
            i=i+1
            arlink = gisat[0]
            artitle = gisat[1][0]
            artext = gisat[1][1]
            arsumy = do_summary.sumy_text(artext, 3)
            aisum=AI_summary.Article2json(arlink)
            koartitle = aisum['Title_Kr']
            koarsumy = aisum['Summary_Kr']
        except Exception as e:
            print (e)
        news.append({'Language':'En','No':i,'Date': today, 'Link': arlink, 'Title': artitle, 'Text': artext,
                        'Summary': arsumy, 'Title_Kr': koartitle, 'Summary_Kr': koarsumy})
    return news

