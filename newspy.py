from newspaper import Article
#크롤링할 url 주소

def news(url,lang='en'):
    
    #한국어이므로 language='ko'
    article = Article(url, language=lang)
    article.download()
    article.parse()
    #기사 제목 가져오기
    artext=article.text.replace(u'\xa0', u' ').replace(u'\n', u' ').replace(u'\u200b', u' ')
    newsarticle=[article.title,artext]
    return newsarticle