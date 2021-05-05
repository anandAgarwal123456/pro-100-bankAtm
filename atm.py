class Atm:
    def __init__(self,user,card_num,pin_num,totalBalance):
        self.card_num = card_num
        self.pin_num = pin_num
        self.user = user
        self.totalBalance = totalBalance

    def balance_inquiry(self):
        print("Your account balance is:" + self.totalBalance)

    def cash_withdrawal(self,amount):
        self.totalBalance = self.totalBalance - amount
        print("You have: "+ str(self.totalBalance) + " in your account")


my_atm = Atm("Anand",43567,201002,1000000)

my_atm.cash_withdrawal(20000)