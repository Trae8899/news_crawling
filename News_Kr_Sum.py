import News_Kr
import telegram_msg  # telepot 모듈 import
import json
import os
from datetime import datetime
import wordwrite_json
import win32com.client



today = datetime.today().strftime('%y%m%d')
userloute=os.path.expanduser('~')
folder_path = os.path.join(userloute, "Documents", "NewsData")
json_path = os.path.join(folder_path, "NewsKr.json")
json_today_path = os.path.join(folder_path, f"NewsKr_{today}.json")

try:
    krnews=News_Kr.News_Json()
    with open(json_path, 'a', encoding='utf-8') as f:
        json.dump(krnews, f, ensure_ascii=False, indent=4)
    with open(json_today_path, 'w', encoding='utf-8') as f:
        json.dump(krnews, f, ensure_ascii=False, indent=4)
except:
    pass

wordpath=wordwrite_json.Json2Word_Titlelink(json_today_path)
wordlinkpath=wordwrite_json.Json2Word_addlink(json_today_path)
wdFormatPDF = 17


word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(wordpath)
outputFile = os.path.join(folder_path, f"오늘Thebell_{today}.pdf")
doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()

telegram_msg.word2msg(wordlinkpath,split_no=20)
telegram_msg.file2msg(outputFile)