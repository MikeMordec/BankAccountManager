'''
Created on Apr 24, 2022

@author: michaelmordec
'''
global balance
global accountOpen
    
def main():
    accountOpen = False
    balance  = 0
    while(True):
        print()
        print("1) open account")
        print("2) deposit")
        print("3) withdraw")
        print("4) balance")
        print("5) Exit")
        choice = int(input("Please enter a number: "))
        if(choice==1):
            print("Hello User!")
            accountOpen = True
            deposit = float(input("Please enter desired deposit: "))
            balance = balance + deposit
        if(choice==2):
            if(accountOpen):
                deposit = float(input("Please enter desired deposit: "))
                balance = balance + deposit        
            else:
                print("Please open an account first.")
        if(choice==3):
            if(accountOpen):
                withdraw = float(input("Please enter desired withdraw ammount: "))
 
                if(balance < withdraw):
                    print("Insufficient Funds")
                else:
                    balance = balance - withdraw 
            else:
                print("Please open an account first.")
        if(choice==4):
            if(accountOpen):
                print("Balance:", balance)
            else:
                print("Please open an account first.")
        if(choice==5):
            break
main()
print("Done.")