#Overloading:
from multipledispatch import dispatch
class Addition:
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)
    @dispatch(int,float)
    def add(self,a,b):
        print(a+b)

p = Addition()
p.add(10,20)
p.add(10,23.2)
