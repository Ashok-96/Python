import smtplib
server=smtplib.SMTP('smpt.gmail.com',587)
server.ehlo()
server.starttls()
server.login('ashokkumarakay96@gmail.com','Akay@1999')
server.sendmail('ashokkumarakay96@gmail.com','ashokkumarakay96@gmail.com','Automated mail from python')
print('sent successfully!!')
server.quit()