import requests
from bs4 import BeautifulSoup
import time

from newAlarm import NewsAssistant

# Slack 
bot = NewsAssistant("뉴스", 30, '[업비트 거래소 뉴스]')

while True:
    # Crawl Data
    url = "https://docs.upbit.com/changelog"
    bs = BeautifulSoup(requests.get(url).text,'html.parser')

    current_news = bs.find("div", attrs={'class': 'ChangelogPost3IWNOaGQe_H1 ChangelogPostExcerpt3aGQ8Xxa74DX'})
    news_main = current_news.find('a')

    news_title = news_main.get_text()
    news_link = news_main.get("href")
    news_link = "https://docs.upbit.com" + news_link

    # Check is it new
    f = open("memory.txt", "r", encoding="UTF-8-sig")
    previous_news = f.read()
    f.close()

    if previous_news != news_title:
        f = open("memory.txt", "w", encoding="UTF-8-sig")
        f.write(news_title)
        f.close()

        # Alarm to user
        bot.post_message(news_title, news_link)


    # 1시간 간격으로 새 뉴스 확인
    time.sleep(60*60)