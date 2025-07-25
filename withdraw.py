from Account import MainAcc

class Debit:

    def withdraw(self):
        amt = float(input('enter the amount to be withdrawn: '))
        avail_debit = MainAcc().bal()
        print ('balance: ',avail_debit)
        if amt > avail_debit:
            print('insufficient funds:',amt,'>',avail_debit)

        else:
            return 'remaining effective balance after withdrawl= ', avail_debit - amt

