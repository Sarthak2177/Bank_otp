from twilio.rest import Client


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(

  body=f'Hello' ,  #message body
  from_='+18153840986', #temporary mobile number from twilio
  to='' # Modile number to send notification
)



