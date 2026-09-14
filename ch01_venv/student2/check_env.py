import sys
import flask
import pymysql
import config

print("파이썬 실행 경로 :", sys.executable)
print("파이썬 버전     :", sys.version.split()[0])
print("Flask 버전      :", flask.__version__)
print("PyMySQL 버전    :", pymysql.__version__)
print("내 포트         :", config.PORT)
print("내 DB 이름      :", config.DB_NAME)
