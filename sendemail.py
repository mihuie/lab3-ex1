import smtplib  

fromname = 'Michael Huie'
toname = 'Michael'
subject = 'Hello there!'
msg = 'This is a test. Is it working?'
fromaddr = 'huie.michael@gmail.com'  
toaddr = 'huie.business@gmail.com'  

header  = 'From: %s\n' % fromaddr
header += 'To: %s\n' % toaddr
header += 'Subject: %s\n\n' % subject
messagetosend = header + msg


# Credentials (if needed)  
username = 'huie.michael@gmail.com'  
password = 'aofbguskyevglfvx'

# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromaddr, toaddr, messagetosend)  
server.quit()

