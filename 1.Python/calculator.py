sign=input("Enter the arithmetic sign: ")
num1=input("Enter your first number: ")
num2=input("Enter your second number: ")
if num2=="0":
    print("Division by zero is not possible")
if(sign=="+"):
    print("The sum is ",int(num1)+int(num2))
elif(sign=="-"):
    print("The difference is ",int(num1)-int(num2))
elif(sign=="*"):
    print("The product is ",int(num1)*int(num2))
elif(sign=="/" and num2!="0"):
    print("The quotient is ",int(num1)/int(num2))