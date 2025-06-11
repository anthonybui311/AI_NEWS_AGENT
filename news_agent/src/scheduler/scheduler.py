from apscheduler.triggers.cron import CronTrigger
from news_agent.configuration.config import *
from apscheduler.schedulers.blocking import BlockingScheduler

def daily_news_job():
    print(f"🤖 Starting daily news job")


def start_scheduler(func: callable, time: str):
    """Start the daily scheduler"""
    scheduler = BlockingScheduler()
    
    # Parse schedule time
    hour, minute = time.split(':')
    
    scheduler.add_job(
        func,
        CronTrigger(hour=int(hour), minute=int(minute))
    )
    
    print(f"🗓️ Scheduler started. Next run: {time} daily")
    scheduler.start()

if __name__ == "__main__":
    # Test the job once
    time = "15:19"
    start_scheduler(daily_news_job, time)