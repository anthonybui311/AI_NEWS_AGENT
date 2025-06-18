from dotenv import load_dotenv #type: ignore
import os

load_dotenv()  # Load variables from .env file

SUMMARY_LENGTH = int(input("Please type in the desired summary length you want: "))  # sentences per topic
MAX_ARTICLES = int(input("Please type in the maximum number of articles you want per topic: "))  # max articles per topic
SCHEDULE_TIME = input("Please type in the time you want to run the job (e.g., '9:00' for every day at 9 AM): ")


OLLAMA_MODEL = "llama3.1:8b"
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL=os.getenv("RECIPIENT_EMAIL")
API_KEY=os.getenv("API_KEY")

NEWS_SOURCES = {
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


# Initialize empty dictionary for news sources
NEWS_SOURCES = {}

# Add news sources
print("\nAdd news sources (Press Ctrl+C or type 'done' to finish):")
try:
    while True:
        topic = input("\nEnter news topic/category (or 'done' to finish): ").strip()
        if topic.lower() == 'done':
            break
            
        url = input(f"Enter the URL for {topic}: ").strip()
        if url:
            NEWS_SOURCES[topic] = url
            print(f"Added {topic} with URL: {url}")
        else:
            print("URL cannot be empty. Please try again.")
            
except KeyboardInterrupt:
    print("\nFinished adding news sources.")

if not NEWS_SOURCES:
    print("No news sources were added. Using default sources...")
    NEWS_SOURCES = {
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
for topic, url in NEWS_SOURCES.items():
    print(f"- {topic}: {url}")