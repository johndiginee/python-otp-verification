"""Simple Python OTP Verification"""
import os
import math
import random
import smtplib

"""
    Generate a random number and store it in a variable
"""
numbers = "0123456789"
OTP = ""

for i in range (6):
    OTP += numbers[math.floor(random.random()*10)]

otp = OTP + " is your OTP"
message = otp

"""
    We need to have our Google app password to be able 
    to send emails using your Gmail account
"""
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

email_address = input("Please enter your email address: ")
s.login("YOUR GMAIL ID HERE", "YOUR APP PASSWORD HERE")
s.sendmail('&&&&&&',email_address,message)

verifyOTP = input("Please your OTP: ")
if verifyOTP == OTP:
    print("Verified")
else:
    print("Invail OTP, Please check your OTP!")