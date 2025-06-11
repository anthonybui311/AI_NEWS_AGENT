#DONE
from news_agent.src.scanner.get_links_and_date import *
from news_agent.src.scanner.web_scraper import *
from news_agent.configuration.config import *

def scrape_news(source:dict, topic:str, max_links:int=10):
    links = scrape_links_and_dates(source[topic], max_links)
    articles = []
    for link in links:
        articles.append(scrape_web(link['link']))
    return articles

if __name__ == "__main__":
    for topic in NEWS_SOURCES.keys():
        articles = scrape_news(NEWS_SOURCES, topic, 5)
        print(f"Topic: {topic}")
        print(*articles, sep="\n\n")
        print("\n\n")
        print("-"*100)
    