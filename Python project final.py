bank_accounts = {
    "1234": {"name": "Sarthak", "image": 'sarthak.jpg', "balance": 12000, "pin": 1234, "mobile_number": ''},
    "5678": {"name": "Ayush", "image": 'ayush.jpg', "balance": 42000, "pin": 1244, "mobile_number": '654210'},
    "9123": {"name": "Arya", "image": 'arya.jpg', "balance": 103211, "pin": 1231, "mobile_number": '68432132'},
    "4325": {"name": "Saish", "image": 'saish.jpg', "balance": 10000, "pin": 1232, "mobile_number": '9862169'}
}

from twilio.rest import Client
import random

# Function to deposit money into a bank account
def deposit(account_number, amount):
    if account_number in bank_accounts:
        bank_accounts[account_number]["balance"] += amount
        print(f"Deposited {amount} into account {account_number}.")
        print(f"New balance is {bank_accounts[account_number]['balance']}.")
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'Deposited {amount} from account {account_number}.New balance is {bank_accounts[account_number]["balance"]}.' ,
            from_='+14437323022',
            to=bank_accounts[account_number]["mobile_number"]
        )
    else:
        print("Account not found.")

# Function to withdraw money from a bank account
def withdraw(account_number, amount):
    if account_number in bank_accounts:
        if bank_accounts[account_number]["balance"] >= amount:
            bank_accounts[account_number]["balance"] -= amount
            print(f"Withdrew {amount} from account {account_number}.")
            print(f"New balance is {bank_accounts[account_number]['balance']}.")
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'Withdrew {amount} from account {account_number}.New balance is {bank_accounts[account_number]["balance"]}.' ,
                from_='+14437323022',
                to=bank_accounts[account_number]["mobile_number"]
            )

        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

# Function to access bank account and perform actions
def access_account(account_number):
    print(f"Welcome, {bank_accounts[account_number]['name']}")
    print("What would you like to do?")
    print("\n1. Deposit amount")
    print("2. Withdraw amount")
    print("3. Check Bank Balance")
    choice = input("Choose an option (1, 2, 3): ")
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        deposit(account_number, amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        withdraw(account_number, amount)
    elif choice == "3":
        print("Your balance is:", bank_accounts[account_number]["balance"])
        print("Thank you!")
    else:
        print("Invalid choice.")

# Function to log in and access bank account information
def login():
    while True:
        account_number = input("Enter your bank account number (or type 'exit' to quit): ")
        if account_number.lower() == "exit":
            print("Exiting program.")
            return None

        if account_number in bank_accounts:
            pin_limit = 0
            while pin_limit < 3:
                pin = int(input("Enter your 4 digit pin: "))

                if pin == bank_accounts[account_number]["pin"]:
                    return account_number
                else:
                    print("Incorrect pin, please try again.")
                    pin_limit += 1

            print("You have reached your maximum pin attempts.")
            print("Enter the OTP sent to your registered mobile number.")

            otp = random.randint(1000, 9999)

            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'Your OTP for bank login verification is {otp}',
                from_='+14437323022',
                to=bank_accounts[account_number]["mobile_number"]
            )

            verify = int(input("Type Your OTP: "))

            if verify == otp:
                print("OTP Verified!")
                return account_number
            else:
                print("Invalid OTP")

                return None
        else:
            print("Invalid account number. Please try again.")

# Entry point of the program
def main():
    account_number = login()
    if account_number:
        access_account(account_number)

if __name__ == "__main__":
    main()
