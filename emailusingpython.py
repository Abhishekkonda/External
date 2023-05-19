import smtplib
from email.message import EmailMessage
subject = "Sending mail using python"
body = "Hi, this is a test mail"
server_email = "smtp.gmail.com"
port_no = 587
sender = "your email"
username = "your email"
password = "your password"
recipient = "recipient email"
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient
msg.set_content(body)
server = smtplib.SMTP(server_email,port_no)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()
print("Email sent successfully")