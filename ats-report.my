#!/usr/bin/python
import loganalysis
import socket
import time
import datetime
import time as t
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from datetime import date
from datetime import time
from datetime import datetime

if __name__ == '__main__' :
	loganalysis.customreportgen()
	loganalysis.errorreportgen()
#	t.sleep(5)
	loganalysis.errorreportgenreq()
#	t.sleep(5)

#t.sleep(2)

# Define these once; use them twice!
strFrom = '<from address>'
strTo = ['<to address 1>', 'to address 2']

temp = datetime.time(datetime.now())
hostname = socket.gethostname()

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = '< {} > ATS CLIENT REPORT {}'.format(hostname, temp)
msgRoot['From'] = strFrom
msgRoot['To'] = ', '.join(strTo)
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<html>\n<body><p>Report image has been attached here.</p><br/><br/><br><img src="cid:resp"><br><img src="cid:error"><br><img src="cid:error2"><br>Thanks  \n<br/><br/><br/><img src="cid:logo" width="130" height="90"><br/>\n<br/><b>Mail System  <br/><br/></b>\n<br/><b>.</p>\n</body>\n</html>', 'html')
msgAlternative.attach(msgText)


fp = open('logo.jpg', 'rb')
logoimg = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
logoimg.add_header('Content-ID', '<logo>')
msgRoot.attach(logoimg)

# This example assumes the image is in the current directory
fp = open('reqs.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<resp>')
msgRoot.attach(msgImage)


fp = open('error.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<error>')
msgRoot.attach(msgImage)


fp = open('error2.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<error2>')
msgRoot.attach(msgImage)



#t.sleep(3)



# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP()
smtp.connect('outlook.office365.com:587')
smtp.starttls()
smtp.login('<username>', '<password>')
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
t.sleep(5)
smtp.quit()
