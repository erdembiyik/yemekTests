import smtplib, os, re, sys, glob, string, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders



attachmentname = 'C:\Users\yigit.cetin\PycharmProjects\Yemek.com\Reports\TestReport.html' #path to an attachment, if you wish

username = 'yigit.cetin@yemeksepeti.com'
password = 'yigit2501'

fromaddr = 'Takiminizin testcisi <yigit.cetin@yemeksepeti.com>' #must be a vaild 'from' addy in your GApps account
toaddr  = 'yigit.cetin@yemeksepeti.com'
replyto = fromaddr #unless you want a different reply-to

msgsubject = 'Test sonuclari hazir!'

htmlmsgtext = """Test raporunu attachment'ta bulabilirsin. Raporu duzgun goruntulebilmek icin indirmen gerekli.<br/>
                    <b>Done!</a>"""

try:

    msgtext = htmlmsgtext.replace('<b>','').replace('</b>','').replace('<br>',"\r").replace('</br>',"\r").replace('<br/>',"\r").replace('</a>','')
    msgtext = re.sub('<.*?>','',msgtext)


    msg = MIMEMultipart()
    msg.preamble = 'This is a multi-part message in MIME format.\n'
    msg.epilogue = ''

    body = MIMEMultipart('alternative')
    body.attach(MIMEText(msgtext))
    body.attach(MIMEText(htmlmsgtext, 'html'))
    msg.attach(body)

    if 'attachmentname' in globals():
        f = attachmentname
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    msg.add_header('From', fromaddr)
    msg.add_header('To', toaddr)
    msg.add_header('Subject', msgsubject)
    msg.add_header('Reply-To', replyto)

    # The actual email sendy bits
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.set_debuglevel(True) #commenting this out, changing to False will make the script give NO output at all upon successful completion
    server.starttls()
    server.login(username,password)
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()

except:
    print ('Email NOT sent to %s successfully. %s ERR: %s %s %s ', str(toaddr), 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2]) )
    #just in case