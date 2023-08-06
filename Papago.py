# 네이버 Papago NMT API 예제
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from get_api import api

def set_chrome_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def papago(text,dest='ko'):
    papago_api=api("NAVER")
    client_id = papago_api['ID']
    client_secret = papago_api['KEY']
    encText = urllib.parse.quote(text)
    data = "source=en&target="+dest+"&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return (response_body.decode('utf-8'))
    else:
        return ("Error Code:" + rescode)
    

def papago_web(text, dest='ko'):
    
    # 웹드라이버 실행 및 페이지 이동
    driver = webdriver.Chrome()

    sentences = re.split(r"[.?!]\s", text)
    translated_sentences=[]
    # 각 문장을 번역한 결과를 저장할 배열 초기화

    # 문장을 하나씩 가져와 번역하고 배열에 저장
    for sentence in sentences:
        # 각 문장 앞뒤 공백 제거
        sentence = sentence.strip()
        
        encoded_text = urllib.parse.quote(sentence)
        url = "https://papago.naver.com/?sk=auto&tk="+dest+"&st="+encoded_text
        driver.get(url)
        # 페이지 로딩 대기 및 조회 버튼 클릭
        time.sleep(1)
        # 페이지 소스 가져오기
        html = driver.page_source
        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html, 'html.parser')
        # 번역 결과 추출
        translated_sentence  = soup.find(id="txtTarget").span.text
        translated_sentences.append(translated_sentence)
    # 드라이버 종료
    driver.quit()

    translated_text=" ".join(translated_sentences)
    
    return translated_text

def papago_translate(text, dest='ko'):
    try:
        driver = webdriver.Chrome()
        url = "https://papago.naver.com/?sk=auto&tk="+dest+"&st="
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.ID,'txtSource').send_keys(text)
        driver.find_element(By.ID,'btnTranslate').click()
        time.sleep(1)
        papago_translated = driver.find_element(By.ID,'targetEditArea')
        result = papago_translated.text
    except Exception as e: # 예외처리 (요소를 찾지 못하는 경우)
        result = e
    finally:
        driver.close()
    return result

def papago_translate_driver(text, dest='ko',driver=webdriver.Chrome() ):
    try:
        url = "https://papago.naver.com/?sk=auto&tk="+dest+"&st="
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.ID,'txtSource').send_keys(text)
        driver.find_element(By.ID,'btnTranslate').click()
        time.sleep(1)
        papago_translated = driver.find_element(By.ID,'targetEditArea')
        result = papago_translated.text
    except Exception as e: # 예외처리 (요소를 찾지 못하는 경우)
        result = e
    return result

# 파파고 번역
def papago_translate_headless(text, dest='ko'):
    try:
        url = "https://papago.naver.com/?sk=auto&tk="+dest+"&st="
        papago = set_chrome_driver()
        papago.get(url)
        time.sleep(1)
        papago.find_element(By.c, 'txtSource').send_keys(text)
        papago.find_element(By.ID, 'btnTranslate').click()
        time.sleep(2)
        papago_translated = papago.find_element(By.ID, 'targetEditArea')
        result = papago_translated.text
    except Exception as e: # 예외처리 (요소를 찾지 못하는 경우)
        result = e
    finally:
        papago.close()
    return result
