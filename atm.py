class Atm(object):
    def __init__(self,cardNumber,pinNumber) :
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber


    def CashWithdrawl(self):
        print("Cash WithDrawel Done")
    def BalanceEnquiry(self):
        print("Contact:283947494")


card1=Atm(1246576,1234567)
print(card1.cardNumber)               
        