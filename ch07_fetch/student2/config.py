import os
from dotenv import load_dotenv

# 위쪽 폴더로 올라가며 .env 파일을 찾아서 읽어옴
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
PORT = int(os.getenv("PORT"))
