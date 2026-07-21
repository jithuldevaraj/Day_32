import smtplib # Imports the built-in library for routing emails

# 1. Define your credentials
my_email = "appbreweryinfo@gmail.com"
password = "vexnarxlphojwuzh" # It is a 16-character App Password, not your main Gmail password.

# 2. Establish the connection:- Creates an object connecting to Gmail's specific SMTP server
connection = smtplib.SMTP("smtp.gmail.com")

# 3. Secure the connection :-  starttls() stands for Transport Layer Security. It encrypts the connection
# so your password and email contents aren't sent across the internet in plain text.
connection.starttls()

# 4. Authenticate :- Logs into the mail server using your email and App Password
connection.login(user=my_email, password=password)

# 5. Send the payload
connection.sendmail(
    from_addr=my_email,                     # The sender
    to_addrs="appbrewerytesting@yahoo.com", # The destination
    msg="Subject:Hello\n\nThis is the body of my email." # The double newline (\n\n) is strictly required by the protocol.
                                                          # It tells the server where the Subject line ends and the Body begins.
)
connection.close() # Close the connection to the server when you are done!


#----------------------------------------Same Code Using With ---------------------------------------------#

import smtplib

# 1. Define your credentials
my_email = "appbreweryinfo@gmail.com"
password = "1234"

# 2. Establish the connection using 'with', The connection will automatically close when this block ends
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()                               # 3. Secure the connection
    connection.login(user=my_email, password=password)  # 4. Authenticate
    connection.sendmail(                                # 5. Send the payload
        from_addr=my_email,
        to_addrs="appbrewerytesting@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

# Once you drop out of the indentation, the connection is automatically severed.
# You do not need to write connection.close()


#----------------------------------Same Code:- Add Attachments(pdf, calc ...) ---------------------------------------#

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# 1. Define your credentials
my_email = "appbreweryinfo@gmail.com"
password = "1234"
receiver_email = "appbrewerytesting@yahoo.com"

# 2. Construct the Multipart Message. This acts as the container for both your text and your file
msg_container = MIMEMultipart()
msg_container['From'] = my_email
msg_container['To'] = receiver_email
msg_container['Subject'] = "Hello, here is your PDF!"

# Attach the text body to the email container
body = "This is the body of my email, and please find the attached file."
msg_container.attach(MIMEText(body, 'plain'))

# 3. Prepare the Attachment
file_to_attach = "document.pdf"  # Replace with your actual file name

# Open the file in 'rb' (read binary) mode. This is required for non-text files like PDFs/Images.
with open(file_to_attach, "rb") as attachment:
    # Create the attachment object
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())

# Encode the file in base64 (this is how files are transmitted over email)
encoders.encode_base64(part)

# Add header information so the receiving email client knows it's an attachment and its name
part.add_header(
    'Content-Disposition',
    f'attachment; filename= {file_to_attach}'
)

# Attach the encoded file to the main email container
msg_container.attach(part)

# 4. Connect and Send
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiver_email,
        msg=msg_container.as_string()  # converts our complex MIME container into the raw text protocol SMTP expects
    )