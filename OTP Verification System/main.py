import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + "is your OTP"
msg = otp
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("YOUR EMAIL", "YOUR PASSWORD")
emailid = input('ENTER YOUR EMAIL ID : ')
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input('ENTER YOUR OTP : ')
if a == OTP:
    print("Verified")
else:
    print("OTP doesn't match! Please check your OTP again")        