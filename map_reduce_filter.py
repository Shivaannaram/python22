from functools import reduce

lst=[1,2,3,4,5,11,6,7,8,9,10]
# def d(a,b):
#     return a*b
# m=map(d,lst)
# print(list(m))
# f=filter(d,lst)
# print(list(f))
# r=reduce(d,lst)
# print(r)
# sum=1
# for i in range(1,11):
#     sum=sum*i
# print(sum)
r=reduce(lambda x,y:x if(x>y)else y,lst)
print(r)
