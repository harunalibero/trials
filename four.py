#LIBERO BANK
name = input("What is your name; ")
balance = 1000
print(f"Hello,{name} your balance is ${balance}.")
am = ("am")
while am:
    print("1.Deposit \n 2.Withdraw \n3.Checkbalance \n4.Exit")
    choose = int(input("What would you like to do: "))
    if choose == 1:
        deposit = int(input("How much would you like to deposit today: "))
        balance = balance + deposit
        print(f"Your new bablance is ${balance}")
    elif choose == 2:
        withdraw = int(input("How much money would you like to withdraw: "))
        if withdraw < balance :
            balance = balance - withdraw 
            print(f"You have withdrawn ${withdraw} and your balance is now ${balance}")
        else:
            print(f"You cant withdraw money that is more than ,${balance} or equal to it.")
    elif choose ==3 :
        print(f"{name},your balance is {balance}.")
    elif choose ==4:
        break
    else:
        print("Invalid choice.")    

