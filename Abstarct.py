from abc import ABC, abstractmethod

class Rbi(ABC):
    @abstractmethod
    def interest(self):
        pass
    def authorization(self):
        print("This is an Authorized bank of RBI")
        print(isinstance(self,Rbi))
    def account_type(self):
        print("This Bank provides different types of accounts.")
        print(isinstance(self,Rbi))

class SBI(Rbi):

    def interest(self):
        print("SBI giving 8% interest")
    def authorization(self):
        print("SBI is an authorized bank of RBI")
    def account_type(self):
        print("SBI Provides Savings and Current Accounts.")

class Axis(Rbi):
    def interest(self):
        print("Axis giving 5% interest")

    def authorization(self):
        print("Axis is an authorized bank of RBI")

    def account_type(self):
        print("Axis Provides Savings and Current Accounts.")

class Iob(Rbi):

    def interest(self):
        print("Iob giving 7% interest")

    def authorization(self):
        print("Iob is an authorized bank of RBI")

    def account_type(self):
        print("Iob Provides Savings and Current Accounts.")


s=SBI()
a=Axis()
i=Iob()
s.interest()
s.account_type()
s.authorization()
a.interest()
a.authorization()
i.interest()
i.authorization()





