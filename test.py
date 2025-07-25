from Savings import savingsaccount
from Transactions.withdraw import Debit
from Transactions.deposite import credit


class t:
    def details(self):
        ch = input("press Y/y to continue N/n to exit")
        while ch != 'N' or ch != 'n':

            print('1) show balance\n 2)Debit\n3)Credit\n')
            ch = int(input("enter your choice: "))
            if ch == 1:
                savingsaccount().showsBalance()
                continue
            elif ch == 2:
                print(Debit().withdraw())
                continue
            elif ch == 3:
                print(credit().Deposite())
                continue
            else:
                print('please enter a valid choice!!!!!')
                continue




