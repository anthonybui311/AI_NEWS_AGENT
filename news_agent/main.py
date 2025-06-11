from news_agent.src.scanner.scraper import scrape_news
from news_agent.src.summarizing.summarizer import summarize_news
from news_agent.src.sending_email.messenger import send_simple_news_email
from news_agent.src.scheduler.scheduler import start_scheduler
from news_agent.configuration.config import *
from logs.logging import setup_logger, log_execution_time
import time

# Initialize logger
logger = setup_logger('news_pipeline')


def process_topic_articles(topic, max_articles=MAX_ARTICLES):
    """Process articles for a specific topic and return summarized articles."""
    try:
        logger.info(f"Processing topic: {topic}")
        articles = scrape_news(NEWS_SOURCES, topic, max_articles)
        
        if not articles:
            logger.info(f"No articles found for topic '{topic}'")
            return []
        
        processed_articles = []
        for i, article in enumerate(articles, 1):
            try:
                if not article.get('Text') or not article['Text'].strip():
                    logger.warning(f"Skipping article {i} - no text content")
                    continue
                
                summarized_text = summarize_news(article['Text'])
                article['Text'] = summarized_text
                processed_articles.append(article)
                logger.info(f"Successfully processed article {i} for topic '{topic}'")
                
            except Exception as e:
                logger.error(f"Error processing article {i} for topic '{topic}': {e}")
                continue
        
        return processed_articles
        
    except Exception as e:
        logger.error(f"Error processing topic '{topic}': {e}")
        return []


@log_execution_time
def daily_news_job():
    """Main job function to process all topics and send emails."""
    logger.info("🤖 Starting daily news job")
    
    processed_topics = 0
    emails_sent = 0
    
    for topic in NEWS_SOURCES.keys():
        articles = process_topic_articles(topic)
        
        if articles:
            try:
                send_simple_news_email(RECIPIENT_EMAIL, topic, articles, "Bản tin hàng ngày")
                emails_sent += 1
                logger.info(f"Successfully sent email for topic '{topic}'")
            except Exception as e:
                logger.error(f"Error sending email for topic '{topic}': {e}")
        
        processed_topics += 1
    
    logger.info(f"🤖 Daily news job completed. Processed {processed_topics} topics, sent {emails_sent} emails")


def main():
    """Main function - starts the scheduled pipeline."""
    try:
        logger.info("Starting news pipeline with scheduler")
        start_scheduler(daily_news_job, SCHEDULE_TIME)
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error in main application: {e}")
    finally:
        logger.info("Application finished")


if __name__ == "__main__":
    main()