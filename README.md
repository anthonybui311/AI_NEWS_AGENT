# AI News Agent

An automated news aggregation and summarization system that scrapes Vietnamese news articles, summarizes them, and delivers the content through various channels.

## 📁 Project Structure

```
AI_News_Agent/                  # Root directory
├── README.md                   # Project documentation
├── main_fast.py               # Fast execution entry point
└── news_agent/                # Main package directory
    ├── __init__.py           # Package initializer
    ├── main.py               # Main application entry point
    ├── requirements.txt      # Project dependencies
    │
    ├── configuration/        # Configuration settings
    │   ├── __init__.py
    │   └── config.py        # Global configuration variables
    │
    ├── src/                 # Source code directory
    │   ├── __init__.py
    │   │
    │   ├── scanner/        # News scraping module
    │   │   ├── __init__.py
    │   │   ├── scraper.py              # Main scraping logic
    │   │   ├── get_links_and_date.py   # URL extraction
    │   │   └── web_scraper.py          # Content extraction
    │   │
    │   ├── summarizing/    # Text summarization module
    │   │   ├── __init__.py
    │   │   ├── summarizer.py           # Basic summarizer
    │   │   └── summarizer_with_progress.py  # Enhanced summarizer
    │   │
    │   ├── scheduler/      # Task scheduling module
    │   │   ├── __init__.py
    │   │   └── scheduler.py            # Scheduling logic
    │   │
    │   └── sending_email/  # Email delivery module
    │       ├── __init__.py
    │       └── messenger.py            # Email sending logic
    │
    ├── logs/              # Log files directory
    │   └── *.log         # Log files
    │
    ├── data/             # Data storage directory
    │   └── ...          # Generated data files
    │
    └── agent_ent/        # Virtual environment directory
        └── ...          # Virtual environment files
```

### 📂 Directory Descriptions

- **`main_fast.py`**: Quick execution entry point for the application
- **`news_agent/`**: Core package containing all project components
  - **`configuration/`**: Contains all configuration settings and parameters
  - **`src/`**: Main source code directory
    - **`scanner/`**: Handles news article scraping and extraction
    - **`summarizing/`**: Processes and summarizes article content
    - **`scheduler/`**: Manages automated task scheduling
    - **`sending_email/`**: Handles email delivery functionality
  - **`logs/`**: Stores application logs
  - **`data/`**: Stores scraped and processed data
  - **`agent_ent/`**: Virtual environment for project dependencies

## Features

- **News Scraping**: Automatically scrapes Vietnamese news articles from VnExpress
- **Content Summarization**: Generates concise summaries of news articles
- **Scheduling**: Automated scheduling of news collection and delivery
- **Multiple Delivery Channels**: Support for email delivery of news summaries

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv news_agent/agent_ent
source news_agent/agent_ent/bin/activate  # For Unix/macOS
```

2. Install dependencies:
```bash
pip install -r news_agent/requirements.txt
```

3. Set up PYTHONPATH (Required):
```bash
export PYTHONPATH="/Users/vietbui/Desktop/Projects/AI_News_Agent:$PYTHONPATH"
```
This step is crucial for the project to work properly. The PYTHONPATH environment variable tells Python where to find the project modules. You can add this line to your shell's startup file (e.g., ~/.bashrc, ~/.zshrc) to make it permanent.

## Usage

### Running the News Scraper
```bash
python -m news_agent.src.scanner.scraper
```

### Running the Summarizer
```bash
python -m news_agent.src.summarizing.summarizer
# or with progress tracking:
python -m news_agent.src.summarizing.summarizer_with_progress
```

### Running the Scheduler
```bash
python -m news_agent.src.scheduler.scheduler
```

## Configuration

The `configuration/config.py` file contains important settings:
- News source URLs
- Summarization parameters
- Scheduling settings
- Email configuration

## Dependencies

Main dependencies include:
- newspaper3k: For article extraction
- beautifulsoup4: For web scraping
- requests: For HTTP requests
- APScheduler: For task scheduling

## Project Status

This is an active project that supports:
- Vietnamese news scraping from VnExpress
- Multi-topic news collection
- Article summarization
- Scheduled operations
- Email delivery system

## Running the Application

To run the complete system:
```bash
python news_agent/main.py  # For basic functionality
# or
python news_agent/main2.py # For enhanced functionality
```

Make sure to configure your settings in `configuration/config.py` before running the application.
