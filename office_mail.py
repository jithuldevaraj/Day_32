

from email.mime.multipart import MIMEMultipart  # Acts as the main container or "envelope" for your email.
                                                # combine multiple different parts (like a text body AND a PDF attachment) into a single message.

from email.mime.text import MIMEText  # Used to create and format the actual text body of your email.
                                      # It tells the receiving email client whether your message is normal string text ('plain') or formatted web text ('html').

from email.mime.base import MIMEBase  # Used to handle the raw data of your file attachments (like PDFs, images, or CSVs).
                                      # It creates a base object where you can load your file's binary data before attaching it to the main envelope.

from email import encoders  # Provides tools to convert (encode) your binary file data into text.
                            # This is required because SMTP was designed to only send plain text characters; this module safely translates your PDF into Base64 text for transmission.

import smtplib
import datetime as dt

# 1. Define your credentials
office_mail = ""
mail_password = ""
receiver_email = ""

# 2. Construct the Multipart Message. This acts as the container for both your text and your file
email_container = MIMEMultipart()
email_container["From"] = office_mail
email_container["To"] = receiver_email
email_container["Subject"] = "This is the Subject"
# Attach the text body to the email container
body = "This is the body"
email_container.attach(MIMEText(body, "plain"))

# 3. Prepare the Attachment
file_to_attach = "Circular- trng for public by LK members-2-7-26.pdf"
with open(file_to_attach, "rb") as attachment:  # Open the file in 'rb' (read binary) mode.
                                                # This is required for non-text files like PDFs/Images.
    part = MIMEBase("application", "octet-stream")
                                                