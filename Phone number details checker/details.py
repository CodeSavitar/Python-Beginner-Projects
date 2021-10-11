import phonenumbers
from tkinter import *
from phonenumbers import carrier, geocoder, timezone



mob_no = input("Enter the mobile number with country code : ")
mob_no = phonenumbers.parse(mob_no)

# Getting the timezone of a phone number 
print(timezone.time_zones_for_number(mob_no))

# Getting the carrier of a phone number
print(carrier.name_for_number(mob_no, "en"))

#Getting the region information
print(geocoder.description_for_number(mob_no, "en"))

# Vaidating a phone number
print("Valid mobile number : ",phonenumbers.is_valid_number(mob_no))

#Checking the possiblilty of a number
print("Checking the possibility of the number : ",phonenumbers.is_possible_number(mob_no))
