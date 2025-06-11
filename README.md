# AI News Agent

**AI News Agent** is a Python application that automatically scrapes the latest news articles from VnExpress, generates concise AI-powered summaries, and delivers them to users via email—just like a personalized daily newsletter. The goal is to help users stay informed with minimal effort, saving time while ensuring they never miss important headlines.

This project combines robust web scraping techniques with advanced natural language processing. It uses a large language model (LLM) to distill lengthy news articles into clear, digestible summaries. The summarized content is then sent directly to subscribers through automated email delivery, making news consumption fast and convenient.

**Technologies Used:**  
- Python 3  
- Web scraping (BeautifulSoup, requests)  
- AI/LLM summarization  
- Email automation (smtplib, email)  

Whether you're a developer interested in automation, a data enthusiast, or simply want to streamline your news intake, AI News Agent offers a practical, beginner-friendly solution for daily news summarization and delivery.

## 🤖 Setting Up Ollama with llama3.1:8b

This project uses Ollama to run the llama3.1:8b model locally for AI-powered news summarization. Here's how to set it up:

### 1. Install Ollama

For macOS:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

For Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

For Windows:
- Download and install from [Ollama's official website](https://ollama.com/download)

### 2. Start Ollama Service

The Ollama service needs to be running for the application to work:
```bash
ollama serve
```
Keep this terminal window open while using the application.

### 3. Pull the Model

In a new terminal window, pull the llama3.1:8b model:
```bash
ollama pull llama3.1:8b
```
This may take a few minutes depending on your internet connection.

### 4. Verify Installation

Test if Ollama and the model are working correctly:
```bash
ollama run llama3.1:8b "Hello, how are you?"
```

### 5. Integration with AI News Agent

The project automatically uses Ollama through its Python client:
- No API keys needed - everything runs locally
- Model configuration is in `news_agent/configuration/config.py`
- Default model is set to `llama3.1:8b`
- Summarization happens in `news_agent/src/summarizing/summarizer.py`

### Troubleshooting

1. If Ollama isn't responding:
   ```bash
   # Check if Ollama service is running
   curl http://localhost:11434/api/tags
   ```

2. If the model is slow:
   - The first run may take longer as the model loads into memory
   - Subsequent runs will be faster
   - Consider reducing the number of articles processed in parallel

3. Memory Issues:
   - llama3.1:8b requires approximately 8GB of RAM
   - Close other memory-intensive applications while running
   - Consider using a lighter model if needed

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
