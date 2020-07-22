import time


def login():
    import time
    print("\t WELCOME !")
    time.sleep(1)
    global username
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    ReadFile = open("Username", 'r')
    for account in ReadFile.readlines():  # checking the text file for user existence
        if username in account and password in account and password != username in account:
            ReadFile.close()
            print("Access granted!")
            break
    else:
        print("Incorrect Login credentials.")
        time.sleep(1)
        OpenAccount = input("Would you like to create an account ?")
        if OpenAccount.lower()[0] == 'y':
            print("NOTICE! \nUser name and password must be different ! ")  # to prevent function (login) issues line 9
            time.sleep(1)
            CreateAccount = open("Username", 'a')
            CreateAccount.write(input("Enter New Account name"))
            CreateAccount.write("   ")
            CreateAccount.write(input("Enter New Password"))
            CreateAccount.write("\n")
            CreateAccount.close()
            print("Done!")
            login()
        else:
            Option1 = input("would you like to try login again ?")
            if Option1.lower()[0] == 'y':
                login()
            else:
                print("Goodbye")


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_balance(self):
        print("Current balance :", self.balance)

    def greet(self):
        print("hello", username)

    def overdraft(self, balance, withdraw):
        if withdraw > balance:
            print("Overdraft")


def main():
    username = BankAccount()
    username.greet()
    username.print_balance()
    print("d for deposit w for withdraw b for balance")
    time.sleep(1)
    action1 = str(input("Please Choose an action"))
    while action1 == 'w' or 'd':
        if action1.lower() == "d":
            try:
                username.deposit(float(input("Please insert amount of money to deposit:")))
                break
            except ValueError as e1:
                print(e1, "input must be a number")
                break  # add retry

        elif action1.lower() == "w":
            try:
                username.withdraw(float(input("Please insert amount of money to withdraw:")))
                break

            except ValueError as e1:
                print(e1)
                break  # add retry
        elif action1.lower() == 'b':
            username.print_balance()
            break

        else:
            print("wrong input")
            action1 = input("Please type w for withdraw or d for deposit or b for balance:")




login()  # user login function "Username.txt" file needed !
main()  # Main function runs the Bank class
