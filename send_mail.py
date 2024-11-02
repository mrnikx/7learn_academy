import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from local_config import PASSWORD

# تابع برای ایجاد گزارش و ذخیره آن در یک فایل متنی
def create_report(filename):
    with open(filename, 'w') as f:
        f.write("this is test message\n")
        f.write("line 1\n")
        f.write("line 2")

# تابع برای ارسال ایمیل با پیوست
def send_email_with_attachment(sender_email, receiver_email, password, subject, body, filename):
    # ایجاد پیام
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # محتوای ایمیل
    msg.attach(MIMEText(body, 'plain'))

    # افزودن پیوست
    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(part)

    # ارسال ایمیل
    try:
        server = smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525)  # سرور SMTP و پورت
        server.starttls()  # شروع TLS
        server.login("13f58d7473ba7c", PASSWORD)
        server.send_message(msg)
        print("ایمیل با موفقیت ارسال شد!")
    except Exception as e:
        print(f"error: {e}")


# پارامترها
sender_email = "your_email@example.com"
receiver_email = "recipient@example.com"
password = PASSWORD  # رمز عبور
report_filename = "report.txt"
subject = "daily report"
body = "check the attachment file"

# ایجاد گزارش و ارسال ایمیل
create_report(report_filename)
send_email_with_attachment(sender_email, receiver_email, password, subject, body, report_filename)
