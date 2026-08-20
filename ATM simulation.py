a=10000.23
print("Welcome")
print("choose any of choise in below:")
print("Deposite(D/d)")
print("Withdraw(W/w)")
print("Check Balance(B/b)")
print("Exit(E/e)")
ch=(input("your choise:"))
if ch=="D" or ch=="d":
    d=int(input("Enter your amount:"))
    print("now your balance is:",a+d)
elif ch=="W" or ch=="w":
    w=int(input("Enter your amount:"))
    print("now your balance is:",a-w)
elif ch=="B" or ch=="b":
    b=int(input("Enter your amount:"))
    print("your balance is:",a)
elif ch=="E" or ch=="e":
    print("exited transaction canceled")
else:
    print("enter valuable option!!!")
print("thank you for visiting!")
