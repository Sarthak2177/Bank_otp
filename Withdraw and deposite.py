# bank_operations.py

# Import necessary data and services from other modules
from bank_data import bank_accounts
from sms_service import send_sms

def deposit(account_number, amount):
    """
    Deposits money into a bank account and sends a confirmation SMS.
    Args:
        account_number (str): The account number to deposit into.
        amount (float): The amount to deposit.
    """
    if account_number in bank_accounts:
        bank_accounts[account_number]["balance"] += amount
        print(f"Deposited {amount} into account {account_number}.")
        print(f"New balance is {bank_accounts[account_number]['balance']}.")
        
        message_body = f'Deposited {amount} to account {account_number}. New balance: {bank_accounts[account_number]["balance"]}.'
        send_sms(bank_accounts[account_number]["mobile_number"], message_body)
    else:
        print("Error: Account not found.")

def withdraw(account_number, amount):
    """
    Withdaws money from a bank account and sends a confirmation SMS.
    Args:
        account_number (str): The account number to withdraw from.
        amount (float): The amount to withdraw.
    """
    if account_number in bank_accounts:
        if bank_accounts[account_number]["balance"] >= amount:
            bank_accounts[account_number]["balance"] -= amount
            print(f"Withdrew {amount} from account {account_number}.")
            print(f"New balance is {bank_accounts[account_number]['balance']}.")
            
            message_body = f'Withdrew {amount} from account {account_number}. New balance: {bank_accounts[account_number]["balance"]}.'
            send_sms(bank_accounts[account_number]["mobile_number"], message_body)
        else:
            print("Error: Insufficient funds.")
    else:
        print("Error: Account not found.")
