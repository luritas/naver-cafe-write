import os
import sys
import pymysql


class Database:
    def __init__(self):
        self.db_hostname = os.environ.get("DB_PG_HOST")
        self.db_name = os.environ.get("DB_PG_NAME")
        self.db_user = os.environ.get("DB_PG_USER")
        self.db_password = os.environ.get("DB_PG_PASSWORD")
        self.connection = None

    def connect(self):
        # MySQL Connection 연결
        try:
            self.connection = pymysql.connect(
                host=self.db_hostname,
                user=self.db_user,
                password=self.db_password,
                db=self.db_name,
                charset='utf8')
        except Exception:
            raise Exception("데이터 베이스 연결 실패")
        # Connection 으로부터 Cursor 생성

    def insert(self, sql, data):
        # data = ( ('홍진우', 1, '서울'), )
        # sql = "insert into customer(name,category,region) values (%s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.executemany(sql, data)
                self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.close()

    def close(self):
        self.connection.close()
