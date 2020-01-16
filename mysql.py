import pymysql
import re

db = pymysql.connect(host='49.233.191.221',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
sql = 'insert into words(word,mean) values(%s,%s);'
