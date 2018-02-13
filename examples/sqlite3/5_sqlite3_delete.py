import sqlite3

# 连接数据库，如果数据库文件不存在，自动创建数据库文件
conn = sqlite3.connect('db.sqlite3')
print('connected database successfully')

# 获取操作游标
c = conn.cursor()

# 删除数据库
c.execute('''
DELETE FROM COMPANY WHERE ID='6'
''')
# 提交事务，如果不提交事务数据不会更新到数据库
conn.commit()
print('Total number of rows deleted :', conn.total_changes)

# 获取数据库
cursor = c.execute('''
SELECT ID,NAME,ADDRESS,SALARY FROM COMPANY
''')
for r in cursor:
    print(r)  # 获取的数据是元祖形式所以用数字下标获取单个数据
    print("ID = ", r[0])
    print("NAME = ", r[1])
    print("ADDRESS = ", r[2])
    print("SALARY = ", r[3], '\n')

# 关闭数据库
conn.close()
print('closed database successfully')
