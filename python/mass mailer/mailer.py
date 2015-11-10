import csv 
import smtplib
from email.mime.text import MIMEText
import re 
import time

#message file --> message.txt
fp = open('message.txt', 'rb')
msg = MIMEText(fp.read())
fp.close()
msg['Subject'] = "Testing"
msg['From'] = 'nikhil1945.singh@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('nikhil1945.singh@gmail.com','password')
#opening the email file
email_data = csv.reader(open('email.csv','rb'))
email_pattern= re.compile("^.+@.+\..+$")
for row in email_data:
    if(email_pattern.search(row[1])):
        del msg['To']
        msg['To'] = row[1]
        try:
            #server.sendmail(fromadr , toadr , message)
            server.sendmail('nikhil1945.singh@gmail.com' , [row[1]], msg.as_string())
        except SMTPException:
            print "An error occured"
            time.sleep(5) #send next mail after 5 seconds
server.quit()
print "Execution completed"
