import os
import json
import requests
from datetime import datetime
import pyecharts
from openai import OpenAI
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
import smtplib


class HotFinanceAnalysor:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
        self.base_url = os.getenv('BASE_URL')
        self.email_sender = os.getenv('EMAIL_SENDER')
        self.email_receiver = os.getenv('EMAIL_RECEIVER')
        self.email_host = os.getenv('EMAIL_HOST')
        self.email_recipients = os.getenv("EMAIL_RECIPIENTS", "").split(",")

        # 数据存储路径
        self.data_dir = "data"
        self.report_dir = "reports"

        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def run(self):
        fetch()

if __name__ == '__main__':
    HotFinanceAnalysor().run()
