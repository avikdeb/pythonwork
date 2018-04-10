import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import datetime
from random import randint
from happybday.bday_selector import *

# Returns randonly selected image file - Note all image must be in .jpg format
def image_selector(imgfile_start_idx, imgfile_end_idx):
    select_idx = randint(imgfile_start_idx, imgfile_end_idx)
    return str(select_idx) + "." + "jpg"

# Returns randomly selected message from the wish file - wishes.txt
def message_selector(msg_wishfile):

    #Open the wish file, reads the lines and populate a list of messages
    with open(msg_wishfile) as file:
        wish_msg_list = file.readlines()
    file.close()

    #Randomly select the message in list and returns the same
    select_msg = wish_msg_list[randint(0, len(wish_msg_list))]
    return  select_msg

# Returns the email of the person whose birthday matches today
def email_selector(bday_excel, date):
    get_emailid_by_date(bday_excel, date)


# Send email with random wish message and random image file to the selected email-id
def send_bday_email(email_id, message, image_file):
    fromaddr = "avikdeb.select@gmail.com"
    # Use actual password - Not shown for security
    password = "XXXXXXXX"
    toaddr = email_id

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Happy Birthday!!"

    msg.attach(MIMEText(message, 'plain'))
    img_data = open(image_file, 'rb').read()
    image = MIMEImage(img_data, name=os.path.basename(image_file))
    msg.attach(image)

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

# Running the program as main
if __name__ == "__main__":
    date = datetime.date.today()
    email_id = get_emailid_by_date("bday.xlsx", date)
    print(email_id)
    message_body = message_selector("wishes.txt") + "\n \n - Python Coding Team" + "  (Email: avikdeb@gmail.com)"
    image_filename = image_selector(1, 12)

    #Checks if valid email-id exists
    if email_id != "" and email_id != None:
        send_bday_email(email_id, message_body, image_filename)
