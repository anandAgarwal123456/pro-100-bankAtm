class Atm:
    def __init__(self,user,card_num,pin_num,totalBalance,cash_withdrawan):
        self.card_num = card_num
        self.pin_num = pin_num
        self.user = user
        self.totalBalance = 6000
        self.cash_withdrawan = 1000
    
    def input_card_pin(self):
        input("Enter your card number:")
        input("Enter you pin number:")

    def balance_inquiry(self):
        print("You have 6000 rupees in your account")

    def cash_withdrawal(self):
        print("Rupees 1000 withdrawn successfully!")

    def money_left(self):
        remaining_balance = self.totalBalance - self.cash_withdrawan
        print("remaining balance in your account is:"+ remaining_balance)