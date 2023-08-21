class Bank:
    def __init__(self,acc_no,balance,phone_no,addr):
        self.acc_no=acc_no
        self.__balance=balance
        self.__phone_no=phone_no
        self.addr=addr
    def get_balance(self):
        print(self.__balance)

    def set_withdraw(self,balance):
        if balance<1000:
            print(self.__balance)
            print('requested withdraw is not possible')
        if balance>=1000:
            self.__balance=self.__balance-balance
            print(self.__balance)
    def set_deposit(self,balance,acc_type):
        if acc_type=='saving':
            self.__balance=self.__balance+balance
            print(self.__balance)
        if acc_type=='current':
            self.__balance=self.__balance+balance
            print(self.__balance)


Cust1=Bank(9576,5000,123455,'hyd')
print(Cust1._Bank__balance)
print(Cust1._Bank__phone_no)
Cust1.set_deposit(2000,'saving')
Cust1.set_withdraw(1000)
