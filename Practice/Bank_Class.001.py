class BankAccount:
    BankAccountName = "Stiller"

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_balance(self):
        print("Current balance is:", self.balance)

    def login(self):
        import time
        print("\t WELCOME !")
        time.sleep(1)
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        ReadFile = open("Username", 'r')
        for account in ReadFile.readlines():  # checking the text file for user existence
            if username in account and password and password != account in account:
                print("Access granted!")
                print("Welcome", username)
                ReadFile.close()
                break
        else:
            print("Incorrect Login credentials, please try again.")
            time.sleep(1)
            OpenAccount = input("Would you like to create an account ?")
            if OpenAccount.lower()[0] == 'y':
                print(
                    "NOTICE! \nUser name and password must be different ! ")  # to prevent function (login) issues line 9
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

