class Atm (object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def CashWithdrawl(self):
        print("CashWithdrawed")

    def BalanceEnquiry(self):
        print("BalanceEnquired")


hdfc=Atm("212107","1818")
hdfc.CashWithdrawl(1000)
hdfc.BalanceEnquiry()

