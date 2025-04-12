from datetime import datetime
import pandas as pd
import random
import smtplib
import os

# Load your email credentials from environment variables for security
MY_EMAIL = os.environ["EMAIL"]
MY_PASSWORD = os.environ["PASSWORD"]

# Get today's date (month and day)
today = datetime.now()
today_tuple = (today.month, today.day)

# Read the birthday data from the CSV file
data = pd.read_csv("birthdays.csv")

# Create a dictionary with keys as (month, day) and values as the row of data
birthdays_dict = {
    (row["month"], row["day"]): row
    for (_, row) in data.iterrows()
}

# Check if today's date matches any birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Choose a random letter template (1 to 3)
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # Replace placeholder with actual name
        personalized_letter = contents.replace("[NAME]", birthday_person["name"])

    # Set up SMTP connection and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday! 🎉\n\n{personalized_letter}"
        )
