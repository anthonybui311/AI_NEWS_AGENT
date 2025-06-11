#DONE
from news_agent.configuration.config import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

    # def send_news_email(recipient_email, news_articles, email_title="Tin tức mới nhất", sender_email=config.EMAIL_ADDRESS, sender_password=config.EMAIL_PASSWORD):
    #     """
    #     Sends an email containing multiple news articles with titles and summaries.
        
    #     Parameters:
    #     - recipient_email (str): The email address of the recipient
    #     - news_articles (list): List of dictionaries containing 'title' and 'summary'
    #     - email_title (str): The subject line of the email
    #     - sender_email (str, optional): Your email address
    #     - sender_password (str, optional): Your app password
        
    #     Returns:
    #     - bool: True if email sent successfully, False otherwise
    #     """
        
    #     try:
    #         # Create HTML email content
    #         html_content = create_news_html(news_articles, email_title)
            
    #         # Create the email message
    #         email_message = MIMEMultipart('alternative')
    #         email_message['From'] = sender_email
    #         email_message['To'] = recipient_email
    #         email_message['Subject'] = email_title
            
    #         # Create HTML part
    #         html_part = MIMEText(html_content, 'html', 'utf-8')
    #         email_message.attach(html_part)
            
    #         # Connect and send email
    #         with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
    #             smtp_server.starttls()
    #             smtp_server.login(sender_email, sender_password)
    #             smtp_server.send_message(email_message)
            
    #         print(f"News email sent successfully to {recipient_email}")
    #         print(f"Sent {len(news_articles)} articles")
    #         return True
            
    #     except Exception as e:
    #         print(f"Error sending news email: {str(e)}")
    #         return False

    # def create_news_html(news_articles, email_title):
    #     """
    #     Creates HTML content for the news email
    #     """
    #     current_date = datetime.now().strftime("%d/%m/%Y")
        
    #     html_content = f"""
    #     <!DOCTYPE html>
    #     <html>
    #     <head>
    #         <meta charset="UTF-8">
    #         <style>
    #             body {{
    #                 font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    #                 line-height: 1.6;
    #                 color: #334;
    #                 max-width: 800px;
    #                 margin: 0 auto;
    #                 padding: 20px;
    #                 background-color: #f5f5f5;
    #             }}
    #             .container {{
    #                 background-color: white;
    #                 padding: 30px;
    #                 border-radius: 10px;
    #                 box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    #             }}
    #             .header {{
    #                 text-align: center;
    #                 border-bottom: 3px solid #2c5aa0;
    #                 padding-bottom: 20px;
    #                 margin-bottom: 30px;
    #             }}
    #             .header h1 {{
    #                 color: #2c5aa0;
    #                 margin: 0;
    #                 font-size: 28px;
    #             }}
    #             .date {{
    #                 color: #666;
    #                 font-size: 14px;
    #                 margin-top: 10px;
    #             }}
    #             .article {{
    #                 margin-bottom: 30px;
    #                 padding: 20px;
    #                 border-left: 4px solid #2c5aa0;
    #                 background-color: #f9f9f9;
    #                 border-radius: 5px;
    #             }}
    #             .article-title {{
    #                 color: #2c5aa0;
    #                 font-size: 18px;
    #                 font-weight: bold;
    #                 margin-bottom: 15px;
    #                 line-height: 1.4;
    #             }}
    #             .article-summary {{
    #                 color: #555;
    #                 font-size: 16px;
    #                 line-height: 1.6;
    #                 text-align: justify;
    #             }}
    #             .article-number {{
    #                 color: #2c5aa0;
    #                 font-weight: bold;
    #                 font-size: 14px;
    #                 margin-bottom: 10px;
    #             }}
    #             .footer {{
    #                 text-align: center;
    #                 margin-top: 40px;
    #                 padding-top: 20px;
    #                 border-top: 1px solid #ddd;
    #                 color: #666;
    #                 font-size: 14px;
    #             }}
    #         </style>
    #     </head>
    #     <body>
    #         <div class="container">
    #             <div class="header">
    #                 <h1>{email_title}</h1>
    #                 <div class="date">Ngày {current_date}</div>
    #             </div>
    #     """
        
    #     # Add each article
    #     for i, article in enumerate(news_articles, 1):
    #         html_content += f"""
    #             <div class="article">
    #                 <div class="article-number">Tin {i}:</div>
    #                 <div class="article-title">{article['title']}</div>
    #                 <div class="article-summary">{article['summary']}</div>
    #             </div>
    #         """
        
    #     html_content += f"""
    #             <div class="footer">
    #                 <p>Tổng cộng: {len(news_articles)} tin tức</p>
    #                 <p><em>Email được gửi tự động từ hệ thống tin tức</em></p>
    #             </div>
    #         </div>
    #     </body>
    #     </html>
    #     """
        
    #     return html_content

def send_simple_news_email(recipient_email, topic, news_articles, subject="Bản tin hàng ngày", sender_email=EMAIL_ADDRESS, sender_password=EMAIL_PASSWORD):
    """
    Simplified function to send news email with plain text format
    """
    try:
        # Create plain text content
        current_date = datetime.now().strftime("%d/%m/%Y")
        message_content = f"{subject}\n🗓️ Ngày {current_date}\n\n"
        message_content += f"📰 Chủ đề: {topic}\n\n"
        message_content += "=" * 50 + "\n\n"
        
        for i, article in enumerate(news_articles, 1):
            message_content += f"📰 Tin {i}:\n"
            message_content += f"📌 Tiêu đề: {article['Title']}\n\n"
            message_content += f"📝 Tóm tắt: {article['Text']}\n\n"
            message_content += f"🔍 Link: {article['Link']}\n\n"
            message_content += "-" * 40 + "\n\n"
        
        message_content += f"📌 Tổng cộng: {len(news_articles)} tin tức\n"
        
        # Create and send email
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = recipient_email
        email_message['Subject'] = subject
        
        body = MIMEText(message_content, 'plain', 'utf-8')
        email_message.attach(body)
        
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)
            smtp_server.send_message(email_message)
        
        print(f"Simple news email sent successfully to {recipient_email}")
        return True
        
    except Exception as e:
        print(f"Error sending simple news email: {str(e)}")
        return False

# Example usage with your news data
def main():
    """
    Example of how to use the news email functions
    """
    
    # Sample news articles (including your example)
    news_articles = [
        {
            "Title": "Bộ Giáo dục yêu cầu các trường đại học rà soát phương thức, tổ hợp xét tuyển",
            "Text": "Tất cả các trường đại học phải rà soát tổ hợp xét tuyển để không ảnh hưởng quyền lợi thí sinh trước kỳ thi tốt nghiệp. Nhiều trường đã thay đổi về phương thức xét tuyển khiến thí sinh lo lắng.",
            "Link": "https://vnexpress.net/bo-giao-duc-yeu-cau-cac-truong-dai-hoc-ra-soat-phuong-thuc-to-hop-xet-tuyen-4895404.html"
        },
        {
            "Title": "Thị trường chứng khoán Việt Nam tăng điểm mạnh trong phiên đầu tuần",
            "Text": "VN-Index tăng 15,2 điểm lên mức 1.235 điểm, thanh khoản cải thiện đáng kể. Các cổ phiếu ngân hàng và bất động sản dẫn dắt thị trường tăng điểm.",
            "Link": "https://vnexpress.net/thi-truong-chung-khoan-viet-nam-tang-diem-manh-trong-phien-dau-tuan-4895404.html"
        },
        {
            "Title": "Dự báo thời tiết: Bắc Bộ có mưa rào và dông rải rác",
            "Text": "Từ ngày mai, khu vực Bắc Bộ có mưa rào và dông rải rác, cục bộ có mưa to. Nhiệt độ cao nhất 28-31 độ C. Người dân cần đề phòng thời tiết bất lợi.",
            "Link": "https://vnexpress.net/du-bao-thoi-tiet-bac-bo-co-mua-rao-va-dong-rai-rac-4895404.html"
        },
        {
            "Title": "Công nghệ AI được ứng dụng rộng rãi trong y tế Việt Nam",
            "Text": "Nhiều bệnh viện lớn đã triển khai các giải pháp AI để hỗ trợ chẩn đoán và điều trị. Công nghệ này giúp nâng cao chất lượng khám chữa bệnh và giảm tải cho đội ngũ y bác sĩ.",
            "Link": "https://vnexpress.net/cong-nghe-ai-duoc-ung-dung-rong-ra-trong-y-te-viet-nam-4895404.html"
        },
        {
            "Title": "Du lịch Việt Nam phục hồi mạnh mẽ sau đại dịch",  
            "Text": "Lượng khách du lịch quốc tế đến Việt Nam tăng 180% so với cùng kỳ năm trước. Các điểm đến như Hạ Long, Phú Quốc, Đà Nẵng thu hút đông đảo du khách.",
            "Link": "https://vnexpress.net/du-lich-viet-nam-phuc-hoi-manh-manh-sau-dai-dich-4895404.html"
        }
    ]
    
        # # Example 1: Send HTML formatted news email
        # print("Sending HTML news email...")
        # success1 = send_news_email(
        #     recipient_email="anthonybui311205@gmail.com",
        #     news_articles=news_articles,
        #     email_title="📰 Bản tin thời sự - Cập nhật mới nhất"
        # )
    
    # Example 2: Send simple text news email
    print("\nSending simple text news email...")
    success2 = send_simple_news_email(
        recipient_email="anthonybui311205@gmail.com",
        news_articles=news_articles,
        subject="📱 Tin tức nổi bật hôm nay",
        topic="Thời sự"
    )
    
    
    print(f"\nResults:")
        # print(f"HTML email: {'✅ Success' if success1 else '❌ Failed'}")
    print(f"Text email: {'✅ Success' if success2 else '❌ Failed'}")

if __name__ == "__main__":
    main()