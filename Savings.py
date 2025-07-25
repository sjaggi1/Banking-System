import Account, FD


class savingsaccount(Account.MainAcc,FD.fixeddeposite):

    def showsBalance(self):
        self.accountDetails()
        print('*****************************************')
        print("Effective Balance: ",self.bal())
        print('*****************************************')
        print(self.total())



