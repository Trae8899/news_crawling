import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from langdetect import detect
import nltk
import Papago
import json

def transtoKO(text,dest='ko'):
    try:
        transtext=Papago.papago_translate_headless(text,dest)
    except:
        try:
            transtext = Papago.papago_translate(text,dest)
        except:
            try:
                papatext = Papago.papago(text,dest)
                response_dict = json.loads(papatext)
                transtext = response_dict['message']['result']['translatedText']
            except:
                translator = Translator()
                transtext = translator.translate(text, dest).text
    return transtext


def detect_lang(text):
    lang = detect(text)
    if lang == "en":
        return "english"
    elif lang == "ko":
        return "korean"
    else:
        return "english"  # 기본 설정을 영어로 합니다.

def sumy_text(text, sentences=3):
    enko = detect_lang(text)
    parser = PlaintextParser.from_string(text, Tokenizer(enko))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences)
    
    summarized_text = '\n'.join([str(sentence) for sentence in summary])

    # for sentence in summary:
    #     print(sentence)
    return summarized_text
    