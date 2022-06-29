import requests
from bs4 import BeautifulSoup
import time



while True:

    url = "https://docs.upbit.com/changelog"
    bs = BeautifulSoup(requests.get(url).text,'html.parser')
    
    #interest = []

    current_news = bs.find("div", attrs={'class': 'ChangelogPost3IWNOaGQe_H1 ChangelogPostExcerpt3aGQ8Xxa74DX'})
    news_main = current_news.find('a')

    print(news_main.get("href"))
    print(news_main.get_text())


    time.sleep(900)