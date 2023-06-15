import csv

class BankAccount:
    def __init__(self, name, accountnumber, balance) -> None:
        self.name = name
        self.accountnumber = accountnumber
        self.balance = balance
        self.save_data(name=self.name, acc_num=self.accountnumber, balance=self.balance)

    def deposit(self, amount):
        if type(amount) != int:
            raise ValueError("invalid deposit ")
        amount = abs(amount)
        self.balance += amount
        print(f"{amount} deposited")
        self.save_data(name=self.name, acc_num=self.accountnumber, balance=self.balance)

    def withdrawal(self, amount):
        amount = abs(amount)
        if amount > self.balance:
            raise ValueError("withdrawal amount cannot be more than balance")
        
        self.balance -= amount
        print(f"{amount} withdrew")
        self.save_data(name=self.name, acc_num=self.accountnumber, balance=self.balance)

    def bank_fees(self, fee = 0.05):
        self.balance = self.balance * (1-fee)
        print(f"{fee}% drawed from account")
        self.save_data(name=self.name, acc_num=self.accountnumber, balance=self.balance)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account number: {self.accountnumber}")
        print(f"Account balance: {self.balance}")

    def save_data(self, name,  acc_num, balance):
        with open("accs.txt", "a+") as accs:
            acc_text = accs.read()
            acc_lines = accs.readlines()
            avail = False
            if str(acc_num) in acc_text:
                for i in range(len(acc_lines)):
                    if str(acc_num) in acc_lines[i]:
                        if dict(acc_lines[i][:-3])["account_number"] == str(acc_num):
                            acc_lines[i] = '{"name":name, "account_number":acc_num, "balance":balance}\n'
                            avail = True

            if not avail:
                acc_lines.append('{"name":name, "account_number":acc_num, "balance":balance}\n')
                

def obj_maker(acc_num):
    with open("accs.txt", "r") as accs:
            acc_text = accs.read()
            acc_lines = accs.readlines()
            avail = False
            if acc_num in acc_text:
                for i in range(len(acc_lines)):
                    if acc_num in acc_lines[i]:
                        dict_acc = dict(acc_lines[i][:-3])
                        if dict_acc["account_number"] == acc_num:
                            obj = BankAccount(name=dict_acc["name"],
                                               accountnumber=dict_acc["account_number"],
                                                 balance=dict_acc["balance"])
                            return obj

                            avail =True
            if not avail:
                raise ValueError("Account number not in database")


acc = BankAccount("mahdi", 12345, 2000)
acc.deposit(1000)
acc.withdrawal(500)
acc.bank_fees()
acc.display()


if __name__ == "__main__":
    while True:
        print("1.Create account")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Bank fees")
        print("5.Display info")
        print("6 for quiting")
        stat = input("Choose a number from menu >>>")
        

        match stat:
            case "6":
                break
            case "1":
                pass
            case "2":
                acc_num = int(input("Enter your account number>>>"))
                acc = obj_maker(acc_num)
                amount = int(input("Enter deposit amount>>>"))
                acc.deposit(amount)
                
                
