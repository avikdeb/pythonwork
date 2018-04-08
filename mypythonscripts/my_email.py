import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "avikdeb.select@gmail.com"
# Use actual password - Not shown for security
password = "XXXXXXXXXXXXXXXX"
toaddr = "avikdeb@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Email from Python3"

body = "This is a test e-mail."
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("[SUCCESS] Email sent")

except:
    print("[ERROR] Email sent failed")