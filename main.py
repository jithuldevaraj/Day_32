import smtplib
import datetime as dt

# 1. Define your credentials
my_email = "studynumber0001@gmail.com"
my_password = "ivtzfbphayzssfmy"

to_email = "kitetvmsouth@gmail.com"

# 2. Establish the connection:- Creates an object connecting to Gmail's specific SMTP server
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()                                  # 3. Secure the connection
    connection.login(user=my_email, password=my_password)  # 4. Authenticate
    connection.sendmail(                                   # 5. Send the payload
        from_addr=my_email,
        to_addrs=to_email,
        msg="Subject: Testing Automation\n\nThis is a test message."
    )