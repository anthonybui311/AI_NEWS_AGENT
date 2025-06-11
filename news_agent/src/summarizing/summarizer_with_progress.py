"""
This module is used to summarize news articles with progress tracking.
"""
#DONE

import json
import ollama
from typing import Dict, List
import re
from config import OLLAMA_MODEL, SUMMARY_LENGTH
from web_scraper import clean_text_advanced
from tqdm import tqdm
import time

def summarize_news(news: str, model: str = OLLAMA_MODEL, show_progress: bool = True) -> Dict[str, str]:
    """
    Summarizes a news article using Ollama and returns title and summary.
    
    Args:
        news (str): The news article text to summarize
        model (str): The Ollama model to use for summarization
        show_progress (bool): Whether to show progress bar
        
    Returns:
        str: Summary of the news article
        
    Raises:
        ValueError: If news is empty or invalid JSON response
        RuntimeError: If Ollama service error occurs
        Exception: For other processing errors
    """
    # Handle empty news article
    if not news or not news.strip():
        raise ValueError("News article is empty")

    # Initialize progress bar for single article processing
    if show_progress:
        pbar = tqdm(total=4, desc="📰 Summarizing Article", 
        bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]')
    
    try:
        # Step 1: Preparing prompt
        if show_progress:
            pbar.set_description("📝 Preparing prompt")
            pbar.update(1)
        
        # Construct the prompt for Ollama - using proper JSON format in examples
        prompt = f"""Bạn là một chuyên gia trong việc tóm tắt tin tức.

                    Với một bài báo được cung cấp, nhiệm vụ của bạn là trích xuất **ý chính** và các **từ khóa quan trọng nhất**.

                    ✅ Hướng dẫn:
                    - Chỉ sử dụng tiếng Việt.
                    - Giữ phần tóm tắt **ngắn gọn và rõ ràng**, độ dài **{SUMMARY_LENGTH} câu**.
                    - Tập trung trả lời các câu hỏi **ai, cái gì, khi nào, ở đâu và tại sao**.
                    - Tránh đưa vào các chi tiết không cần thiết, ý kiến cá nhân, hoặc nội dung rườm rà.
                    - Giảm thiểu lỗi sai, thông tin bịa đặt và ngôn ngữ không phải tiếng Việt.

                    🧾 Đầu ra:
                    - **Chỉ trả về một chuỗi văn bản** là phần tóm tắt nội dung bài báo, không kèm bất kỳ tiêu đề, định dạng JSON hay giải thích nào.

                    Bây giờ hãy tóm tắt bài báo sau:

                    {news}

                    🔁 **Chỉ trả về phần tóm tắt ngắn gọn bằng tiếng Việt. Không kèm theo bất kỳ định dạng nào khác.**

                """
        
        # Step 2: Sending to Ollama
        if show_progress:
            pbar.set_description("🤖 Processing with AI")
            pbar.update(1)
        
        # Use ollama.generate for JSON-only output
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        
        # Step 3: Processing response
        if show_progress:
            pbar.set_description("⚙️ Processing response")
            pbar.update(1)
        
        # Extract and parse response
        response_text = response.get("response", "").strip()
        cleaned_response = clean_text_advanced(response_text)
        
        # Step 4: Finalizing
        if show_progress:
            pbar.set_description("✅ Complete")
            pbar.update(1)
            pbar.close()
        
        return cleaned_response

    except Exception as e:
        if show_progress:
            pbar.set_description("❌ Error occurred")
            pbar.close()
        
        if isinstance(e, (ValueError, RuntimeError)):
            raise
        raise Exception(f"An error occurred while processing the news article: {str(e)}")
    
def main():
    news = """
                Bộ Giáo dục: Tất cả đại học phải rà soát tổ hợp xét tuyển. Các trường đại học phải rà soát phương thức, tổ hợp xét tuyển để không ảnh hưởng quyền lợi thí sinh trước kỳ thi tốt nghiệp, theo Bộ Giáo dục. Bộ Giáo dục và Đào tạo đưa ra yêu cầu trên chiều 6/6. Lý do là nhiều thí sinh phản ánh một số trường công bố thông tin tuyển sinh chưa đầy đủ. "Có một số thông tin thay đổi phần nào gây tâm lý lo lắng, bị động cho thí sinh", cơ quan này cho hay. Ngoài rà soát phương thức, tổ hợp xét tuyển phù hợp với từng ngành, chương trình, các trường phải đảm bảo công bằng, không làm ảnh hưởng tới thí sinh, khi các em đã đăng ký thi tốt nghiệp THPT xong. Nếu thay đổi về phương thức, tổ hợp xét tuyển, các trường phải giải trình với xã hội. Thí sinh thi tốt nghiệp THPT năm 2024 tại TP HCM. Ảnh: Quỳnh Trần Sáng nay, Thứ trưởng Hoàng Minh Sơn cho biết đã đề nghị một số trường bỏ xét tuyển bằng tổ hợp C00 (Văn, Sử, Địa) phải rà soát, điều chỉnh, trong đó có trường Đại học Khoa học Xã hội và Nhân văn, Đại học Quốc gia Hà Nội. Trường này báo bỏ xét tổ hợp C00 cách đây hai ngày, với 17 ngành, như Báo chí, Xã hội học, Tâm lý học,... Thay vào đó là các khối D14 (Văn, Sử, Anh), D15 (Văn, Địa, Anh), D66 (Văn, Giáo dục công dân, Anh). Một số trường như Luật (Đại học Quốc gia Hà Nội), Học viện Báo chí và Tuyên truyền, Đại học Mở Hà Nội... ra thông báo tương tự trước đó. Nhiều thí sinh, phụ huynh phản ứng vì cho rằng kỳ thi tốt nghiệp THPT đã cận kề. Thí sinh năm nay thi hai môn bắt buộc là Toán, Ngữ văn, cùng hai môn lựa chọn và đã đăng ký từ cuối tháng 4. Có em xác định xét bằng tổ hợp C00 nên không thi Ngoại ngữ, giờ "trở tay không kịp". Kỳ thi tốt nghiệp THPT diễn ra ngày 26-27/6, điểm thi được công bố ngày 16/7. Thí sinh đăng ký nguyện vọng xét tuyển đại học từ 16/7 đến 28/7. Hồi tháng 4, Bộ từng yêu cầu các trường đại học rà soát khi một số trường dùng các tổ hợp lạ để xét tuyển ngành Sư phạm, Y khoa, Ngôn ngữ. Chẳng hạn, có trường tuyển ngành Sư phạm Vật lý nhưng dùng tổ hợp không có môn Vật lý; Y khoa không dùng tổ hợp có môn Hóa và Sinh. Dương Tâm
                """
    
    print("=== Single Article Example ===")
    try:
        result = summarize_news(news)
        print(f"Summary: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print("\n=== Multiple Articles Example ===")
    # Example with multiple articles
    sample_news = [news, news[:500], news[500:1000]]  # Using parts of the same article as example
    try:
        summaries = summarize_multiple_news(sample_news)
        for i, summary in enumerate(summaries, 1):
            print(f"Article {i} Summary: {summary[:100]}...")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
