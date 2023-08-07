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
            if inv_no==6:
                break
            inv_no += 1
            try:
                gisa.append(investing[0])
            except:
                continue
    except:
        pass

    #Market Watch
    try:
        Mw_hot = Marketwatch_POP()
        mw_no=0
        for marketW in Mw_hot:
            if mw_no==6:
                break
            mw_no += 1
            try:
                gisa.append(marketW[0])
            except:
                continue
    except:
        pass
    #CNBC
    try:
        cnbc_hot = CNBC_POP()
        cnbc_no=0
        for cnbc in cnbc_hot:
            if cnbc_no==6:
                break
            cnbc_no += 1
            try:
                gisa.append(cnbc[0])
            except:
                continue
    except:
        pass
    #Cnn
    # try:
    #     cnn_hot = Cnn_pop()
    #     cnn_no=0
    #     for cnn in cnn_hot:
    #         if cnn_no==6:
    #             break
    #         cnn_no += 1
    #         try:
    #             gisa.append(cnn[0])
    #         except:
    #             continue
    # except:
    #     pass
    #reuter
    try:
        reuters_hot = Reuters_pop()
        for reuter in reuters_hot:
            try:
                gisa.append(reuter[0])
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
            arlink = gisat
            artitle =newspy.news(arlink,"en")[0]
            aisum=AI_summary.Article2json(arlink)
            koartitle = aisum['Title_Kr']
            koarsumy = aisum['Summary_Kr']
            hits=aisum['Views']
            news.append({'Language':'En','Date': today, 'Link': arlink, 'Title': artitle, 'Title_Kr': koartitle, 'Summary_Kr': koarsumy,'Hits':hits})
        except Exception as e:
            print (e)
            continue
        news.sort(key=lambda x: x['Hits'], reverse=True)

    
    return news

