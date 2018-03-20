import os
import pymysql

def connect():
    hostname = os.environ.get("DB_PG_HOST")
    dbname = os.environ.get("DB_PG_NAME")
    user = os.environ.get("DB_PG_USER")
    password = os.environ.get("DB_PG_PASSWORD")

        # MySQL Connection 연결
    connect = pymysql.connect(host=hostname, user=user, password=password, db=dbname, charset='utf8')
    # Connection 으로부터 Cursor 생성
    return connect

