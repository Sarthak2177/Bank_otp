from twilio.rest import Client
import random

otp = random.randint(1000,9999)

account_sid = ''#account sid  here
auth_token = ''#auth token here
client = Client(account_sid, auth_token)

message = client.messages.create(

  body=f'Your OTP for bank login varification is {otp}' ,
  from_='+14437323022', #temporary mobile number by twilio
  to=''
)

verify=int(input("Type Your OTP: "))

if verify==otp:
    print("Verified!")

else :
    print("Invalid OTP")