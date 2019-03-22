class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


# another class inheritance
class Checking(Account):
    type_data = "checking"

    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking("bankdemo/balance.txt", 5)
print(checking.type_data)
checking.transfer(10)
checking.commit()
print(checking.balance)