import requests
from bs4 import BeautifulSoup
import time

while True:
    # Crawl Data
    url = "https://docs.upbit.com/changelog"
    bs = BeautifulSoup(requests.get(url).text,'html.parser')

    current_news = bs.find("div", attrs={'class': 'ChangelogPost3IWNOaGQe_H1 ChangelogPostExcerpt3aGQ8Xxa74DX'})
    news_main = current_news.find('a')

    news_link = news_main.get("href")
    new_title = news_main.get_text()

    # Check is it new
    f = open("memory.txt", "r", encoding="UTF-8-sig")
    previous_news = f.read()
    f.close()

    if previous_news != new_title:
        f = open("memory.txt", "w", encoding="UTF-8-sig")
        f.write(new_title)
        f.close()

        # Alarm to user
        print("새 뉴스가 있습니다.")


    time.sleep(60*60)