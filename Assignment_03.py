# 03.Input principle, rate and time and calculate simple interest

# principle=float(input("Enter the Principal amount: "))
# rate=float(input("Enter the rate: "))
# time=float(input("Enter the Time: "))
# SI=(principle*rate*time)/100
# print("Simple interest is:",SI)


# # 04.Input temperature in Fahrenheit and convert it into degree Centigrade
# fahrenheit=float(input("Enter the Temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32)*5/9
# print("celsius is: ",celsius)

#05.Input any number and check it is b/w 11 and 23
#
# num=float(input("Enter any number: "))
# if(num>=11 and num<=23):
#     print(num,"is in between 11 and 23")
# else:
#     print("Number is out of range")

#06.Input three numbers and find the greatest.
#
# num1 = float(input("Enter the first Number: "))
# num2 = float(input("Enter the second Number: "))
# num3 = float(input("Enter the third Number: "))
#
# if num1 == num2 and num2 == num3:
#     print(" Numbers are equal ")
# elif num1 > num2 and num1 > num3:
#     print(num1, " is the large Number")
# elif num2 > num3:
#     print(num2, " is the large Number")
# else:
#     print(num3, " is the large Number")

#07.Input any number and find its factorial.

# num=int(input("Enter the Number: "))
# fact=1
# for i in range(1,num+1):
#     fact = fact*i
# print(num, "factorial is", fact)

#08.Input any number and display its table.

num=int(input("Enter the number: "))
if num>0:
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
