import os
import sys
import pymysql
import pprint


class Database:
    def __init__(self):
        self.db_hostname = os.environ.get("DB_NAVER_HOST")
        self.db_name = os.environ.get("DB_NAVER_NAME")
        self.db_user = os.environ.get("DB_NAVER_USER")
        self.db_password = os.environ.get("DB_NAVER_PASSWORD")
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

    def select(self, sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                print("쿼리를 실행했습니다")
                return cursor.fetchall()
        except Exception as e:
            print(e)
            self.connection.close()

    def insert(self, sql, data):
        try:
            with self.connection.cursor() as cursor:
                cursor.executemany(sql, data)
                self.connection.commit()
            print("쿼리를 실행했습니다")
        except Exception as e:
            print(e)
            self.connection.close()

    def close(self):
        self.connection.close()
