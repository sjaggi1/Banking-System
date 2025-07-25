from Transactions import deposite
import Account


class New(deposite.credit, Account.MainAcc):

    # def newfile(self):
    #     x = self.Deposite()
    #     print('balance after updation: ', x)

    def __init__(self):
        print('balance before updation', self.bal())
        self.__balance = self.Deposite()
        print('balance after updation: ', self.__balance)


New()
