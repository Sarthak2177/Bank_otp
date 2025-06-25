# main_app.py

# Import necessary components from other modules
from bank_data import bank_accounts
from bank_operations import deposit, withdraw
from otp_service import generate_otp, verify_otp
from sms_service import send_sms

def access_account(account_number):
    """
    Provides a menu for bank account operations (deposit, withdraw, check balance).
    Args:
        account_number (str): The authenticated account number.
    """
    print(f"\nWelcome, {bank_accounts[account_number]['name']}!")
    print("What would you like to do?")
    print("\n1. Deposit amount")
    print("2. Withdraw amount")
    print("3. Check Bank Balance")
    
    choice = input("Choose an option (1, 2, 3): ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount < 0:
                print("Deposit amount cannot be negative. Please enter a positive number.")
            else:
                deposit(account_number, amount)
        except ValueError:
            print("Invalid input. Please enter a numerical amount.")
    elif choice == "2":
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount < 0:
                print("Withdrawal amount cannot be negative. Please enter a positive number.")
            else:
                withdraw(account_number, amount)
        except ValueError:
            print("Invalid input. Please enter a numerical amount.")
    elif choice == "3":
        print(f"Your current balance is: {bank_accounts[account_number]['balance']}.")
        print("Thank you for checking your balance!")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

def login():
    """
    Handles the user login process with PIN and OTP verification.
    Returns:
        str or None: The account number if login is successful, otherwise None.
    """
    while True:
        account_number = input("Enter your bank account number (or type 'exit' to quit): ").strip()
        if account_number.lower() == "exit":
            print("Exiting program.")
            return None

        if account_number in bank_accounts:
            pin_attempts = 0
            while pin_attempts < 3:
                try:
                    pin = int(input("Enter your 4-digit PIN: "))
                    if pin == bank_accounts[account_number]["pin"]:
                        print("PIN verified successfully!")
                        return account_number
                    else:
                        print(f"Incorrect PIN. You have {2 - pin_attempts} attempts remaining.")
                        pin_attempts += 1
                except ValueError:
                    print("Invalid PIN format. Please enter a 4-digit number.")
            
            # If PIN attempts exhausted, proceed to OTP
            print("Maximum PIN attempts reached. Initiating OTP verification.")

            user_mobile = bank_accounts[account_number]["mobile_number"]
            if not user_mobile:
                print("No mobile number registered for this account. Cannot send OTP. Login failed.")
                return None

            generated_otp = generate_otp()
            otp_message = f'Your OTP for bank login verification is: {generated_otp}'
            
            # Attempt to send OTP via SMS
            print(f"Sending OTP to {user_mobile}...") # For debugging purposes, remove in production
            if send_sms(user_mobile, otp_message):
                try:
                    user_entered_otp = int(input("Enter the OTP sent to your mobile number: "))
                    if verify_otp(user_entered_otp, generated_otp):
                        print("OTP Verified Successfully! Logging in...")
                        return account_number
                    else:
                        print("Invalid OTP. Login failed.")
                        return None
                except ValueError:
                    print("Invalid OTP format. Login failed.")
                    return None
            else:
                print("Failed to send OTP. Please ensure Twilio is configured correctly and the mobile number is valid. Login failed.")
                return None

        else:
            print("Invalid account number. Please try again.")

def main():
    """
    Entry point of the bank account management program.
    Initializes the login process and then calls the account access menu.
    """
    print("Welcome to the Simple Bank Account Management System!")
    authenticated_account_number = login()
    if authenticated_account_number:
        access_account(authenticated_account_number)
    print("\nThank you for using our service! Goodbye.")

if __name__ == "__main__":
    main()
