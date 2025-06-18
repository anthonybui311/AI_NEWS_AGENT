from dotenv import load_dotenv #type: ignore
import os

load_dotenv()  # Load variables from .env file

def get_user_configs():
    """Get all user configurations through CLI inputs"""
    print("\n=== Configuration Setup ===")
    
    # Get summary length
    while True:
        try:
            summary_length = int(input("\nPlease enter desired summary length (number of sentences per topic): "))
            if summary_length > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    # Get maximum articles
    while True:
        try:
            max_articles = int(input("\nPlease enter maximum number of articles per topic: "))
            if max_articles > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    # Get schedule time
    schedule_time = input("\nPlease enter the time to run the job (e.g., '9:00' for every day at 9 AM): ").strip()

    # Initialize empty dictionary for news sources
    news_sources = {}

    # Add news sources
    print("\nAdd news sources (Press Ctrl+C or type 'done' to finish):")
    try:
        while True:
            topic = input("\nEnter news topic/category (or 'done' to finish): ").strip()
            if topic.lower() == 'done':
                break
                
            url = input(f"Enter the URL for {topic}: ").strip()
            if url:
                news_sources[topic] = url
                print(f"Added {topic} with URL: {url}")
            else:
                print("URL cannot be empty. Please try again.")
                
    except KeyboardInterrupt:
        print("\nFinished adding news sources.")

    if not news_sources:
        print("\nNo news sources were added. Using default sources...")
        news_sources = {
            "Thế giới": "https://vnexpress.net/the-gioi",
            "Thời sự": "https://vnexpress.net/thoi-su",
            "Kinh doanh": "https://vnexpress.net/kinh-doanh",
            "Góc nhìn": "https://vnexpress.net/goc-nhin",
            "Giải trí": "https://vnexpress.net/giai-tri",
            "Thể thao": "https://vnexpress.net/the-thao",
            "Pháp luật": "https://vnexpress.net/phap-luat",
            "Giáo dục": "https://vnexpress.net/giao-duc",
            "Sức khỏe": "https://vnexpress.net/suc-khoe",
            "Đời sống": "https://vnexpress.net/doi-song",
            "Du lịch": "https://vnexpress.net/du-lich",
            "Khoa học công nghệ": "https://vnexpress.net/khoa-hoc-cong-nghe",
        }

    print("\nFinal news sources:")
    for topic, url in news_sources.items():
        print(f"- {topic}: {url}")

    return summary_length, max_articles, schedule_time, news_sources

# Get user configurations
SUMMARY_LENGTH, MAX_ARTICLES, SCHEDULE_TIME, NEWS_SOURCES = get_user_configs()

# Other configurations
OLLAMA_MODEL = "llama3.1:8b"
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
API_KEY = os.getenv("API_KEY")