# DONE
import newspaper
import re
def scrape_web(url: str):  
    """
    Scrape a web page and return the article text.

    Args:
        url (str): The URL of the web page to scrape

    Returns:
        dict: A dictionary containing the article text, title.
    """
    try:
        article = newspaper.Article(url=url, language='vi')
        article.download()
        article.parse()

        article ={
            "Title": clean_text_advanced(article.title),
            "Text": clean_text_advanced(article.text),
            "Link": url
        }
        return article
    
    except Exception as e:
        return {
            "Title": "Error",
            "Text": f"Failed to scrape the article: {str(e)}",
            "Link": url
        }

def clean_text_advanced(text):
    """
    Advanced text cleaning with better paragraph preservation.
    
    Args:
        text (str): The text to clean
        
    Returns:
        str: Cleaned text with proper paragraph breaks
    """
    # Replace double newlines (paragraph breaks) with placeholder
    text = re.sub(r'\n\n+', ' ', text)
    
    # Replace single newlines with spaces
    text = re.sub(r'\n', ' ', text)
    
    # Clean up excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Final cleanup
    text = text.strip()
    
    return text


def main():
    url = "https://vnexpress.net/bo-giao-duc-tat-ca-dai-hoc-phai-ra-soat-to-hop-xet-tuyen-4895404.html"
    article = scrape_web(url)
    print(article)


if __name__ == "__main__":
    main()