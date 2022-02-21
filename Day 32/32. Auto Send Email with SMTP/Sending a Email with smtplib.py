# # Sending a Email with smtplib
# import smtplib
#
# MY_EMAIL = "oliveira.guilherme1994@gmail.com"
# PASSWORD = ""  # Complete using a valid password
#
# with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="guilhermeoliveira.94@hotmail.com",
#         msg="Subject:Email de teste\n\nBoa tarde. Email enviado atraves da biblioteca smtplib em python."
#     )

# # Working with datetime lib
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# hour = now.hour
# day_of_the_week = now.weekday()
#
# if year == 2022:
#     print("Wear a face mark")
#
# date_of_birth = dt.datetime(year=1994, month=4, day=14, hour=23)
# print(date_of_birth)

# Scheduling a motivational email to monday
import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

