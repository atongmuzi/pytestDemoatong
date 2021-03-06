import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading
from common.logger import logger

import zipfile
import glob


class Email:
    def __init__(self):
        global host, user, password, port, sender, title, content
        host = "smtp.163.com"
        user = "jazx505@163.com"
        password = "FXUTNMWPAADLCVDN"
        port = 25
        sender = "jazx505@163.com"
        title = "hahahheheh"
        content = "test"
        self.value = "395624925@qq.com"
        self.receiver = ["395624925@qq.com"]
        # get receiver list
        for n in str(self.value).split("/"):
            self.receiver.append(n)
        # defined email subject
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = title + " " + date
        # self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('mixed')

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        content_plain = MIMEText(content, 'plain', 'utf-8')
        self.msg.attach(content_plain)

    # def config_file(self):
    #     # if the file content is not null, then config the email file
    #     if self.check_file():
    #
    #         reportpath = self.log.get_result_path()
    #         zippath = os.path.join(readConfig.proDir, "result", "test.zip")
    #         # zip file
    #         files = glob.glob(reportpath + '\*')
    #         f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
    #         for file in files:
    #             f.write(file)
    #         f.close()
    #
    #         reportfile = open(zippath, 'rb').read()
    #         filehtml = MIMEText(reportfile, 'base64', 'utf-8')
    #         filehtml['Content-Type'] = 'application/octet-stream'
    #         filehtml['Content-Disposition'] = 'attachment; filename="test.zip"'
    #         self.msg.attach(filehtml)
    #
    # def check_file(self):
    #     reportpath = self.log.get_report_path()
    #     if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
    #         return True
    #     else:
    #         return False

    def send_email(self):
        self.config_header()
        self.config_content()
        # self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
            logger.info("The test report has send to developer by email.")
        except Exception as ex:
            logger.error(str(ex))

class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    email = MyEmail.get_email()
    email.send_email()