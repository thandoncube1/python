def transaction(amount: float, account_number: int, transaction_type: str) -> str:
    """
    :param amount:
    :param account_number:
    :param transaction_type:
    :return: Statement about the transaction to the user
    - Description: This is a regular function encapsulating two processes
    - The DEPOSIT and the WITHDRAW process all running on the same account
    """
    match transaction_type:
         case "DEPOSIT":
             if amount > 20:
                     return f"Deposited ${amount:.2f} to account: {account_number}."
             else:
                 return f"Can't deposit ${amount:.2f} to account: {account_number}."
         case "WITHDRAW":
             if amount >= 20:
                     return f"Withdraw ${amount:.2f} from account: {account_number}."
             else:
                 return f"Can't withdraw ${amount:.2f} from account: {account_number} \nSee Cashier inside!"
         case _:
            return "Thank you for your business, take your card."


def main():
    print("""
      1) New Transaction - DEPOSIT:
      2) New Transaction - WITHDRAW:
      3) VIEW Receipt
     """)
    choice = int(input("Enter a choice: "))
    match choice:
        case 1:
            account = int(input("Enter 4 digit account number: "))
            amount = float(input("Enter the amount you want to deposit: "))
            result = transaction(amount, account, "DEPOSIT")
            with open(f"receipt-{account}.txt", "w") as file:
                 file.write("-----------------------------\n")
                 file.write("----------Reciept------------\n")
                 file.write(f"Account: {account}\n")
                 file.write(f"{result}\n")
                 file.write("-----------------------------\n")
        case 2:
             account = int(input("Enter 4 digit account number: "))
             amount = float(input("Enter the amount you want to withdraw: "))
             result = transaction(amount, account, "WITHDRAW")
             with open(f"receipt-{account}.txt", "a") as file:
                     file.write(f"Account: {account}\n")
                     file.write(f"{result}\n")
                     file.write("-----------------------------\n")
        case 3:
             account = int(input("Enter 4 digit account number: "))
             with open(f"receipt-{account}.txt", "r") as file:
                     for line in file:
                         print(line)