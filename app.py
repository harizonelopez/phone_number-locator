import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+254769405130")
phone_number2 = phonenumbers.parse("+918878586271")
phone_number3 = phonenumbers.parse("+12136574429")
phone_number4 = phonenumbers.parse("+201234567890")
phone_number5 = phonenumbers.parse("+917294536271")
phone_number6 = phonenumbers.parse("+254798954395")

print("\nPhone Number Location")
print("1.", geocoder.description_for_number(phone_number1, "en"));
print("2.", geocoder.description_for_number(phone_number2, "en"));
print("3.", geocoder.description_for_number(phone_number3, "en"));
print("4.", geocoder.description_for_number(phone_number4, "en"));
print("5.", geocoder.description_for_number(phone_number5, "en"));
print("6.", geocoder.description_for_number(phone_number6, "en"));
