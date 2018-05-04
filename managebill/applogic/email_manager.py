import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email_id, message):
    fromaddr = "avikdeb.select@gmail.com"
    # Use actual password - Not shown for security
    password = "XXX"
    toaddr = email_id

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ManageBill Admin - Password Successfully Reset"

    msg.attach(MIMEText(message, 'plain'))
    print("[INIT] Password reset initiated. Preparing to send email")
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