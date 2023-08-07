import openpyxl
from openpyxl import Workbook
import json
import os

def json2excel(filepath):
    path=os.path.dirname(filepath)
    name, _ = os.path.splitext(os.path.basename(filepath))
    wb = Workbook()
    ws = wb.active
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    ws.append(['Lang','No','날짜', '링크', '한국어 제목', '한국어 요약'])
    for item in data:
        ws.append([item['Language'],item['No'],item['Date'], item['Link'], item['Title_Kr'], item['Summary_Kr']])
    doc1_name = os.path.join(path, f"{name}.xlsx")
    wb.save(doc1_name)