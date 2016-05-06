# coding=utf-8
import time
from TestScenarios import *
import HTMLTestRunner

import smtplib, os, re, sys, glob, string, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders




###test suite olusturmak ve html rapor hazırlanmasi

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LogInTests))
    suite.addTest(unittest.makeSuite(RegisterTests))
    #dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    #buf = file("C:\Users\yigit.cetin\PycharmProjects\Yemek.com\Reports\TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    buf = file("C:\Users\yigit.cetin\PycharmProjects\Yemek.com\Reports\TestReport.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            title='Test Report',
            description='Result of tests'
            )
    EmailHtml = runner.run(suite)


###mail gonderimi buradan

# me == my email address
# you == recipient's email address
me = 'Takiminizin testcisi <yigit.cetin@yemeksepeti.com>'
you = "<yigit.cetin@yemeksepeti.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test sonuclari hazir!"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Test"
html = EmailHtml

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# The actual email sendy bits

username = 'yigit.cetin@yemeksepeti.com'
password = 'yigit2501'

server = smtplib.SMTP('smtp.gmail.com:587')
server.set_debuglevel(True) #commenting this out, changing to False will make the script give NO output at all upon successful completion
server.starttls()
server.login(username,password)
server.sendmail(msg['From'], [msg['To']], msg.as_string())
server.quit()
