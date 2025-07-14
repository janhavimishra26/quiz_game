#1st proj
def add(num1,num2):
   return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2!=0:
        return num1/num2
    else:
        return "error"
while True:
    num1=float(input("enter a number"))
    operator=input("enter operator(+,-,/,*)")
    num2=float(input("enter a number"))
    
    if operator =='+':
     print("result", add(num1,num2))
    elif operator=='-':
     print("result", subtract(num1,num2))
    elif operator=='*':
     print("result", multiplication(num1,num2))
    elif operator=='/':
          print("result", division(num1,num2))
    else:
        print("Invalid operator")
    choice=input("do you want to continue?(yes/no)")
    if choice.lower()!='yes':
       print("thank you for using the calculator")
       break