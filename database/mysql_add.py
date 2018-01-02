# encoding=utf-8
import pymysql

try:
    conn = pymysql.connect(host='localhost', port=3306, db='test',
                           user='root', passwd='123456', charset='utf8')
    cs1 = conn.cursor()
    count = cs1.execute("insert into student(name) values('linxinzhe')")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print(e.message)
