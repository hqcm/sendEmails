import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class SendEmail:
    "发送邮件"

    def __init__(self):
        self.host = "smtp.qq.com"
        self.sender = "1973132883@qq.com"
        self.psd = "XXXXXXXXXX"  #qq邮箱的16位授权码
        self.subject = "A test email from python"

    def sendEmail(self, name, receiver):
        "发送邮件"
        msg = MIMEMultipart()  #默认mixed,邮件可以包括纯文本正文，超文本正文，内嵌资源，附件
        #msg['Date']默认一般为当前时间，一般不用设置
        msg['Subject'] = self.subject
        msg['From'] = "黑崎草莓" + "<" + self.sender + ">"
        msg['To'] = receiver
        #添加文字"
        mail_msg = (
            "<p>亲爱的" + name + "：</p>"  #用()进行多行拼接字符串
            """
        <p>这是Python的一个邮件发送测试...</p>
        <p>图片演示：</p>
        <p><img src="cid:image1"></p>
        """)  #写多行字符串时，要采用3个单引号或双引号
        msg.attach(MIMEText(mail_msg, _subtype='html', _charset='utf-8'))
        #添加图片
        #vscode中的相对路径是按照vscode中的文件夹来确认的，当打开此文件夹时，下面的文件能够读取成功，
        #但如果只是打开一个单独的py文件，则会读取失败，即加不加使用getcwd得到的当前路径并不相同
        with open("Barcelona.jpg", "rb") as f:
            image = f.read()
        image = MIMEImage(image)
        #定义图片的ID，在HTML文本中引用，以在文中显示图片
        image.add_header('Content-ID', '<image1>')
        msg.attach(image)
        with open("Barcelona.jpg", "rb") as f:
            image = f.read()
        image_att = MIMEImage(image)
        image_att[
            "Content-Disposition"] = 'attachment; filename="testimage.jpg"'
        msg.attach(image_att)
        #添加图片和txt附件
        with open("test.txt", "rb") as f:
            file = f.read()
        txt_att = MIMEText(file, 'base64', 'utf-8')
        txt_att["Content-Type"] = 'application/octet-stream'
        txt_att["Content-Disposition"] = 'attachment; filename="zh.txt"'
        #附件名称为中文时的写法
        #txt_att.add_header("Content-Disposition", "attachment", filename=("gbk", "", "附件.txt"))
        #txt_att["Content-Disposition"] = 'attachment; filename=("gbk", "", "附件.txt")'
        msg.attach(txt_att)
        try:
            #实例化
            #加密SMTP会话，先创建SSL安全连接，然后再使用SMTP协议发送邮件
            server = smtplib.SMTP_SSL()
            #连接邮箱服务器
            #启用SSL发信,端口一般是465
            server.connect(self.host, 465)
            #登录时用户名为邮箱；采用授权码作为登录密码（需要预先授权开启smtp服务）
            server.login(self.sender, self.psd)
            #发送邮件
            server.sendmail(self.sender, receiver, msg.as_string())
            #断开连接
            server.close()
            print("发送邮件成功！")
            return True
        except smtplib.SMTPException as e:
            print("发送邮件失败：" + str(e))
            return False
        except Exception as e:
            print("发送邮件失败：" + str(e))
            return False


if __name__ == '__main__':
    sendemail = SendEmail()
    name = "黑崎草莓"
    receiver = "1973132883@qq.com"
    sendemail.sendEmail(name, receiver)
