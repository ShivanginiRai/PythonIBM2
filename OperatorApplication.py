#WAP to input operator and 2 numbers and based on operator perform operatons
op=input("Enter the operator")
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if(op=='+'):
      print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    print(a/b)
elif(op=='%'):
     print(a%b)
elif(op=='//'):
    print(a//b)
elif(op=='**'):
    print(a**b)
