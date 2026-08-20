a=10000.23
print("====ATM====")
print("Welcome")
print("choose any of choise in below:")
print("1.Deposite")
print("2.Withdraw")
print("3.Check Balance")
print("4.Exit")
ch=(input("your choise:"))
if ch=="1":
    d=int(input("Enter your amount:"))
    print("now your balance is:",a+d)
elif ch=="2":
    w=int(input("Enter your amount:"))
    print("now your balance is:",a-w)
elif ch=="3":
    b=int(input("Enter your amount:"))
    print("your balance is:",a)
elif ch=="4":
    print("exited!!")
    print("transaction canceled")
else:
    print("enter valuable option!!!")
print("thank you for visiting!")
