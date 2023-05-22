import random
import smtplib
import datetime as dt

MY_EMAIL = "vivekshar2000@gmail.com"
PASSWORD = "Vivek @2000"

date = dt.datetime.now()
day_of_week = date.weekday()

if day_of_week == 0:

    with open("quotes.txt") as file:
        content = file.readlines()

    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="vivekrockss111@gmail.com",
                            msg=f"subject:Monday Motivation\n\n{random.choice(content)}"
                            )
