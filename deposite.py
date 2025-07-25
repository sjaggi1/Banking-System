from Account import MainAcc

class credit:

    def Deposite(self):
        amt = float(input('enter the amount to be credited: '))
        avail = MainAcc().bal()
        print('balance: ', avail)
        avail1 = avail + amt
        return avail1



