Num1 =float(input("Enter the first digit:"))
Num2 =float(input("Enter the seconf number:"))
operation =input("Enter an operation(+,-,*,/):")
if operation=='+':
    result=Num1+Num2
elif operation=='-':
    result=Num1-Num2
elif operation=='*':
    result=Num1*Num2
elif operation=='/':
    if Num2!=0:
     result=Num1/Num2
    else:
     result="Error!Division is by zero" 
else:
 result="invalid operation"
print(f"{Num1} {operation}{Num2} = {result}")
