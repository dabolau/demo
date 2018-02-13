import sqlite3

# 连接数据库，如果数据库文件不存在，自动创建数据库文件
conn = sqlite3.connect('db.sqlite3')
print('connected database successfully')

# 获取操作游标
c = conn.cursor()
# 执行数据库
c.execute('''
INSERT INTO COMPANY
(ID,NAME,AGE,ADDRESS,SALARY)
VALUES
(6,'Paul',32,'California',20000.00)
''')

# 提交事务
conn.commit()
print('commited database successfully')
# 关闭数据库
conn.close()
print('closed database successfully')
