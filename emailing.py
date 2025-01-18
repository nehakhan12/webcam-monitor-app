import smtplib
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
SENDER = os.getenv("EMAIL_ADDRESS")
RECIEVER = os.getenv("EMAIL_ADDRESS")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("PORT"))


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP(SMTP_SERVER, PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/")
