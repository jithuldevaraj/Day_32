import pandas
import datetime as dt
import os
import random
import smtplib

now = dt.datetime.now()

birthday_df = pandas.read_csv("birthdays.csv")
# print(birthday_df["month"][0])



for index, row in birthday_df.iterrows(): # ഓരോ വരിയായി (row) ലൂപ്പ് ചെയ്യുന്നു
  if row["month"] == now.month and row["day"] == now.day: # മാസവും ദിവസവും ഇന്നത്തെ തിയ്യതിയുമായി ഒത്തുനോക്കുന്നു

    #-------------------------------------------random pick a letter----------------------------------------------------
    folder_path = "letter_templates"  # നിങ്ങളുടെ ഫോൾഡറിന്റെ പേര് ഇവിടെ നൽകുക
    txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]  # .txt ഫയലുകൾ തിരഞ്ഞെടുത്ത്
                                                                            # ഒരു ലിസ്റ്റാക്കുന്നു-> ['letter_1.txt',....]
    chosen_file = random.choice(txt_files)  # letter_1.txt # ലിസ്റ്റിൽ നിന്ന് റാൻഡം ആയി ഒരു ഫയൽ തിരഞ്ഞെടുക്കുന്നു
    full_path = os.path.join(folder_path, chosen_file)  # letter_templates\letter_1.txt
                                                        # ഫയലിന്റെ പൂർണ്ണമായ പാത്ത് (Path) നിർമ്മിക്കുന്നു

    # ആ ഫയൽ തുറന്നു വായിക്കാൻ:
    with open(full_path, "r") as file:
        letter_content = file.read()
        new_letter = letter_content.replace("[NAME]", row["name"])

# ---------------------------------------------------Mail Handling-------------------------------------------------------
    # 1. Define your credentials
    my_email = "studynumber0001@gmail.com"
    my_password = "------------"

    # 2. Establish the connection:- Creates an object connecting to Gmail's specific SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # 3. Secure the connection
        connection.login(user=my_email, password=my_password)  # 4. Authenticate
        connection.sendmail(  # 5. Send the payload
            from_addr=my_email,
            to_addrs=row["email"],
            msg=f"Subject: Happy B'day....\n\n{new_letter}"
        )