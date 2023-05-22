import datetime as dt
import os
import random
import smtplib

import pandas

LETTER_TEMPLATE = random.choice(os.listdir("letter_templates/"))
PLACEHOLDER = "[NAME]"
MY_EMAIL = "vivekrockss111@gmail.com"
PASSWORD = "hnddatolzulkfcpz"

date = dt.datetime.now()
today_month = date.month
today_day = date.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): [row["name"], row["email"]] for (index,row) in data.iterrows()}


if today in birthday_dict:
    birthday_name = (birthday_dict[today][0])
    birthday_email = (birthday_dict[today][1])
    print(birthday_name, birthday_email)

    with open(f"letter_templates/{LETTER_TEMPLATE}", mode="r") as file:
        content = file.read()
        letter = content.replace(PLACEHOLDER, birthday_name)

    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_email,
                            msg=f"subject:Happy Birthday!\n\n{letter}")
