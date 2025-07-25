
class MainAcc:
    name = 'ABC'
    address = 'sector 17'
    IFSC_code = '1290897199420'
    branch = 'SBI sector 17'
    accountNumber = 1930298456330
    __balance = 20000

    # def __init__(self):
    #     print('balance before updation', self.__balance)
    #     self.__balance = self.newfile()
    #     print('balance after updation: ',self.__balance)


    def bal(self):
        return self.__balance

    def accountDetails(self):
        print('Account Details: ', '\n', self.name, '\n', self.accountNumber, '\n',
              self.branch, '\n', self.IFSC_code, '\n', self.address)


MainAcc()