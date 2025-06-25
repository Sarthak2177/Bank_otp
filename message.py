# sms_service.py

from twilio.rest import Client

# Your Twilio Account SID, Auth Token, and Twilio Phone Number
# IMPORTANT: Replace these placeholders with your actual Twilio credentials.
TWILIO_ACCOUNT_SID = '' # Your Twilio Account SID
TWILIO_AUTH_TOKEN = ''  # Your Twilio Auth Token
TWILIO_PHONE_NUMBER = '+14437323022' # Your Twilio phone number (e.g., from Twilio dashboard)

def send_sms(to_number, message_body):
    """
    Sends an SMS message using Twilio.
    Args:
        to_number (str): The recipient's mobile number (e.g., '+1234567890').
        message_body (str): The content of the SMS message.
    Returns:
        bool: True if message sent successfully, False otherwise.
    """
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
        print("Twilio credentials (Account SID or Auth Token) are not set. Cannot send SMS.")
        return False
    if not TWILIO_PHONE_NUMBER:
        print("Twilio phone number is not set. Cannot send SMS.")
        return False
    if not to_number:
        print("Recipient mobile number is empty. Cannot send SMS.")
        return False

    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"SMS sent successfully to {to_number}. SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False
