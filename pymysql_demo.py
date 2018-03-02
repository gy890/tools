# coding=utf-8
"""
Created on 2017-05-17

@Filename: pymysql_demo
@Author: Gui


"""
import pymysql.cursors
from datetime import datetime

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='gy890224',
                       db='guest',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor
                       )

try:
    with conn.cursor() as cursor:
        # sql = 'INSERT INTO  sign_guest (realname, phone, email, sign, event_id, create_time) values (%s, %s, %s, %s, %s, %s);'
        # cursor.execute(sql, ("allen", "124545", "allen@mail.com", 0, 1, datetime(2016, 8, 10, 14, 0, 0)))
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id, create_time) VALUES("alen", 18800110001, "alen@mail.com", 0, 1, NOW()); '
        cursor.execute(sql)
        conn.commit()
    with conn.cursor() as cursor:
        sql = 'SELECT realname, phone, email, sign, create_time from sign_guest WHERE phone=%s;'
        cursor.execute(sql, ('124545',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()
