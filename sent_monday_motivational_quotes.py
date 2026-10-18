import datetime as dt
import smtplib
import random

#Date and Time Check
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    # Quotes Data Handling
    with open("quotes.txt", encoding="utf-8") as quote_file:
        quotes = quote_file.readlines() # convert to a list
        quote = random.choice(quotes)

    # Email Handling
    my_email = ""
    password = ""
    to_email = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #Secure the connection
        connection.login(user=my_email, password=password) #Authenticate
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: Monday Motivational Quotes ! \n\n {quote}"
        )

