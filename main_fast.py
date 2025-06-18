from news_agent.src.scanner.scraper import scrape_news
from news_agent.src.summarizing.summarizer import summarize_news
from news_agent.src.sending_email.messenger import send_simple_news_email
from news_agent.src.scheduler.scheduler import start_scheduler
from news_agent.configuration.config import *
import time


def daily_news_job():
    print("🤖 Starting daily news job")
    for topic in NEWS_SOURCES.keys():
        articles = scrape_news(NEWS_SOURCES, topic, 4)
        if not articles:
            continue
        result = []
        for article in articles:
            try:    
                summarized_articles = summarize_news(article['Text'])
                article['Text'] = summarized_articles
                result.append(article)
            except Exception as e:
                print(f"Error summarizing article: {e}")
                continue
        # print(topic, result, sep="\n\n")
        send_simple_news_email(RECIPIENT_EMAIL, topic, result, "Bản tin hàng ngày")
    
    print("🤖 Daily news job completed")

def pipeline_simple(): 
    time = SCHEDULE_TIME
    start_scheduler(daily_news_job, time)

def main():
    pipeline_simple()

if __name__ == "__main__":
    main()
    