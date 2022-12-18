#09.Input any number and find sum of digits

# num=int(input("Enter a number: "))
# sum=0
# while(num>0):
#     dig=num%10
#     sum=sum+dig
#     num=num//10
# print("Sum of digits is:",sum)

#10.Find Fibonacci numbers

num=int(input("Enter a number: "))
def fib(num):
   if num <= 1:
       return num
   else:
       return(fib(num-1) + fib(num-2))

if num <= 0:
   print("Enter a valid Number")
else:
   for i in range(num):
       print(fib(i))