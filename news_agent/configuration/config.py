from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

OLLAMA_MODEL = "llama3.1:8b"
SUMMARY_LENGTH = 3  # sentences per topic
SCHEDULE_TIME = "9:00"  # 9:00 AM daily
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL=os.getenv("RECIPIENT_EMAIL")
API_KEY=os.getenv("API_KEY")

NEWS_SOURCES = {
    # "Thế giới": "https://vnexpress.net/the-gioi",
    # "Thời sự": "https://vnexpress.net/thoi-su",
    # "Kinh doanh": "https://vnexpress.net/kinh-doanh",
    # # "Góc nhìn": "https://vnexpress.net/goc-nhin",
    # # "Giải trí": "https://vnexpress.net/giai-tri",
    # "Thể thao": "https://vnexpress.net/the-thao",
    # # "Pháp luật": "https://vnexpress.net/phap-luat",
    # "Giáo dục": "https://vnexpress.net/giao-duc",
    # # "Sức khỏe": "https://vnexpress.net/suc-khoe",
    # # "Đời sống": "https://vnexpress.net/doi-song",
    # # "Du lịch": "https://vnexpress.net/du-lich",
    "Khoa học công nghệ": "https://vnexpress.net/khoa-hoc-cong-nghe",
    }