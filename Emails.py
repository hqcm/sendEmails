import pymysql

# 初始化连接配置
ConnectConfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'Zh13102030032',
    'charset': 'utf8',
}

# 创建连接对象
db = pymysql.connect(
    host=ConnectConfig['host'],
    port=ConnectConfig['port'],
    user=ConnectConfig['user'],
    passwd=ConnectConfig['passwd'],
    charset=ConnectConfig['charset'],
)

# 创建游标对象
cursor = db.cursor()
cursor.execute('show databases')
rows = cursor.fetchall()
name = "Emails"
cursor.execute('create database if not exists ' + name)
# 如果没有数据库则创建
cursor.execute('use ' + name)
# 创建数据表
cursor.execute("create table Emails(name varchar(20),Email varchar(20));")
# 添加记录
cursor.execute("alter table Emails modify name char(20) character set utf8;"
               )  #汉字的编码问题，本地没有设置正确
rows = [('黑崎草莓', '1973132883@qq.com'), ('黑崎草莓', '1973132883@qq.com')]
cursor.executemany('insert into Emails values(%s,%s);', rows)
db.commit()
cursor.close()
db.close()