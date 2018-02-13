import sqlite3

# 连接数据库，如果数据库文件不存在，自动创建数据库文件
conn = sqlite3.connect('db.sqlite3')
print('opened database successfully')
# 在数据库中创建一个表
c = conn.cursor()
c.execute('''
CREATE TABLE COMPANY
(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL
);
''')
print('created table successfully')
# 提交事务
conn.commit()
# 关闭数据库
conn.close()
