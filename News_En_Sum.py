import News_En_Openai
import telegram_msg  # telepot 모듈 import
import json
import os
from datetime import datetime
import wordwrite_json
import win32com.client



today = datetime.today().strftime('%y%m%d')
userloute=os.path.expanduser('~')
folder_path = os.path.join(userloute, "Documents", "NewsData")
json_path = os.path.join(folder_path, "News.json")
json_today_path = os.path.join(folder_path, f"News_{today}.json")

try:
    ennews=News_En_Openai.News_Json()
    with open(json_path, 'a', encoding='utf-8') as f:
        json.dump(ennews, f, ensure_ascii=False, indent=4)
    with open(json_today_path, 'w', encoding='utf-8') as f:
        json.dump(ennews, f, ensure_ascii=False, indent=4)
except:
    pass

wordpath=wordwrite_json.Json2Word_Titlelink(json_today_path)
wordlinkpath=wordwrite_json.Json2Word_addlink(json_today_path)
wdFormatPDF = 17

word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(wordpath)
outputFile = os.path.join(folder_path, f"밤 사이 미국뉴스_{today}.pdf")
doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()

telegram_msg.msg("해외뉴스 Top 10")
telegram_msg.word2msg(wordlinkpath,tot=2)
telegram_msg.file2msg(outputFile)