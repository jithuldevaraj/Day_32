import os
import random
import pandas
import datetime as dt

now = dt.datetime.now()

birthday_df = pandas.read_csv("birthdays.csv")


for (index, row) in birthday_df.iterrows():
    if now.month == int(row["month"]) and now.day == int(row["day"]):
    #-------------------------------------------random pick a letter----------------------------------------------------
        folder_path = "letter_templates" # നിങ്ങളുടെ ഫോൾഡറിന്റെ പേര് ഇവിടെ നൽകുക
        txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")] #  .txt ഫയലുകൾ തിരഞ്ഞെടുത്ത്
                                                                                        # ഒരു ലിസ്റ്റാക്കുന്നു-> ['letter_1.txt',....]
        chosen_file = random.choice(txt_files) #letter_1.txt # ലിസ്റ്റിൽ നിന്ന് റാൻഡം ആയി ഒരു ഫയൽ തിരഞ്ഞെടുക്കുന്നു
        full_path = os.path.join(folder_path, chosen_file) #letter_templates\letter_1.txt
                                                           # ഫയലിന്റെ പൂർണ്ണമായ പാത്ത് (Path) നിർമ്മിക്കുന്നു

        # ആ ഫയൽ തുറന്നു വായിക്കാൻ:
        with open(full_path, "r") as file:
            content = file.read()
            final_letter = content.replace("[NAME]", row["name"])


#---------------------------------------------------Mail Handling-------------------------------------------------------
