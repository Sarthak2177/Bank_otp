

# Function to deposit money into a bank account
def deposit(account_number, amount):
    if account_number in bank_accounts:
        bank_accounts[account_number]["balance"] += amount
        print(f"Deposited {amount} into account {account_number}.")
        print(f"New balance is {bank_accounts[account_number]['balance']}.")
    else:
        print("Account not found.")

# Function to withdraw money from a bank account
def withdraw(account_number, amount):
    if account_number in bank_accounts:
        if bank_accounts[account_number]["balance"] >= amount:
            bank_accounts[account_number]["balance"] -= amount
            print(f"Withdrew {amount} from account {account_number}.")
            print(f"New balance is {bank_accounts[account_number]['balance']}.")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

# Function to access bank account and perform actions
def access_account(account_number):
    print(f"Welcome, {bank_accounts[account_number]['name']}")
    print("What would u like to do?")
    print("\n1. Deposit amount")
    print("2. Withdraw amount")
    print("3. Check Bank Balance")
    choice = input("Choose an option (1., 2. , 3.): ")
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        deposit(account_number, amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        withdraw(account_number, amount)
    elif choice == "3":
        print("Your balance is:", bank_accounts[account_number]["balance"])
    else:
        print("Invalid choice.")


