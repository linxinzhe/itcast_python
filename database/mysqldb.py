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

try:
    conn = pymysql.connect(host='localhost', port=3306, db='test1', user='root', passwd='mysql', charset='utf8')
    cs1 = conn.cursor()
    count = cs1.execute("update student set name='刘邦' where id=1")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print(e.message)

try:
    conn = pymysql.connect(host='localhost', port=3306, db='test1', user='root', passwd='mysql', charset='utf8')
    cs1 = conn.cursor()
    count = cs1.execute("delete from student where id=1")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print(e.message)

try:
    conn = pymysql.connect(host='localhost', port=3306, db='test1', user='root', passwd='mysql', charset='utf8')
    cs1 = conn.cursor()
    sname = input("请输入学生姓名：")
    params = [sname]
    count = cs1.execute('insert into student(name) values(%s)', params)
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print(e.message)
