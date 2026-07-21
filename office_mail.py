import smtplib

from email.mime.multipart import MIMEMultipart  # Acts as the main container or "envelope" for your email.
                                                # combine multiple different parts (like a text body AND a PDF attachment)
                                                # into a single message.

from email.mime.text import MIMEText  # Used to create and format the actual text body of your email.
                                      # It tells the receiving email client whether your message is normal string text
                                      # ('plain') or formatted web text ('html').

from email.mime.base import MIMEBase  # Used to handle the raw data of your file attachments (like PDFs, images, or CSVs).
                                      # It creates a base object where you can load your file's binary data before attaching
                                      # it to the main envelope.

from email import encoders  # Provides tools to convert (encode) your binary file data into text.
                            # This is required because SMTP was designed to only send plain text characters;
                            # this module safely translates your PDF into Base64 text for transmission.


# 1. Define your credentials
office_mail = ""
mail_password = ""
receiver_email = ""

# 2. Construct the Multipart Message. This acts as the container for both your text and your file
email_container = MIMEMultipart()
email_container["From"] = office_mail
email_container["To"] = receiver_email
email_container["Subject"] = "Test HTML_7"
# Attach the text body to the email container
body = "This is the body"
email_container.attach(MIMEText(body, "plain"))  # _subtype: "plain", "html"

# 3. Prepare the Attachment
file_to_attach = "Screenshot.png"
with open(file_to_attach, "rb") as attachment:  # Open the file in 'rb' (read binary) mode.
                                                # This is required for non-text files like PDFs/Images.
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)  # Encode the file in base64 (this is how files are transmitted over email)
# Add header information so the receiving email client knows it's an attachment and its name
part.add_header("Content-Disposition", f"attachment; filename = {file_to_attach}")
email_container.attach(part)  # Attach the encoded file to the main email container

# 4. Connect and Send
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # tls(Transport Layer Security) encrypts the connection
    connection.login(user=office_mail, password=mail_password)  # Authenticate :- Logs into the mail server
                                                                # using your email and App Password
    connection.sendmail(from_addr=office_mail,
                        to_addrs=receiver_email,
                        msg=email_container.as_string()) # converts our complex MIME container
                                                         # into the raw text protocol SMTP expects
