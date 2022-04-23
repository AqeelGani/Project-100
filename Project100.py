class bankAtm:
    def __init__(self, cardNo, pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo
        self.fixedBalance = 10000

    def balanceEnquiry(self):
        print('Your Account Balance Is', self.fixedBalance)

    def cashWithdrawal(self, amount):
        self.fixedBalance = self.fixedBalance - amount
        print('Withdrawal Successful!\nYour New Account Balance Is ',
              self.fixedBalance)

    def cashDeposit(self, amount):
        self.fixedBalance = self.fixedBalance + amount
        print('Deposit Successful!\nYour New Account Balance Is ', self.fixedBalance)


def main():
    print('Welcome To The XYZ Bank!')
    cn = input('Enter Your Card Number : ')
    pn = input('Enter Your Pin Number : ')
    option = ''

    customer = bankAtm(cn, pn)

    while option != '4':
        print('Press 1 For Balance Enquiry\nPress 2 For Cash Withdrawal\nPress 3 For Cash Deposit\nPress 4 To Quit')
        option = input('Enter Your Choice : ')
        if option == '1':
            customer.balanceEnquiry()
        elif option == '2':
            amt = int(input('Enter The Amount : '))
            customer.cashWithdrawal(amt)
        elif option == '3':
            amt = int(input('Enter The Amount : '))
            customer.cashDeposit(amt)
        elif option == '4':
            print('Thank You For Co-operating With XYZ bank!\nWe Hope To See You Again Soon.')
            break
        else:
            print('Invalid Choice')


main()
