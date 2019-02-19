from sendEmail import SendEmail
import pymysql
import time
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
cursor = db.cursor()
cursor.execute('show databases')
name = "Emails"
cursor.execute('use ' + name)
# 查询Emails表中所有记录
cursor.execute('select * from Emails')
emails = cursor.fetchall()
faillist = []
flag = True
#逐一发送邮件
for email in emails:
    sendemail = SendEmail()
    flag = sendemail.sendEmail(email[0], email[1])
    if not flag:
        faillist.append(email)
    time.sleep(2)
cursor.close()
db.close()
print("共发送失败" + str(len(faillist)) + "个")
