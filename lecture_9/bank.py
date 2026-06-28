# Fourth Example

class Account: 
    def __init__(self):
        self._balance = 0

    @property # recall @property is for Getter method
    def balance(self):
        return self._balance    

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance ", account.balance)

if __name__ == "__main__":
    main()

# use object oriented programming practices as a solution
# typically global variables are frowned upon within the language

# Fourth Example - introduce keyword global

# balance = 0
# 
# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)
# 
# def deposit(n):
#     global balance
#     balance += n
# 
# def withdraw(n):
#     global balance
#     balance -= n
# 
# if __name__ == "__main__":
#     main()
# 
# # this now works but there is a better way to do this global tracking of value in variable

# Third Example

# def main():
#     balance = 0 # balance moved inside of main
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)
# 
# def deposit(n):
#     balance += n
# 
# def withdraw(n):
#     balance += n
# 
# if __name__ == "__main__":
#     main()
# 
# # this code is no good either

# Second Example

# balance = 0 # apparently read is a thing but not write
# 
# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)
# 
# def deposit(n):
#     balance += n
# 
# def withdraw(n):
#     balance += n
# 
# if __name__ == "__main__":
#     main()
# 
# # this code produces an UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value

# First Example - global variables

# balance = 0
# 
# def main():
#     print("Balance: ", balance)
# 
# if __name__ == "__main__":
#     main()

