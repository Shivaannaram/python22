# class Parent1:
#     def d1(self):
#         print("Parent 1 Class")
# class Parent2:
#     def d2(self):
#         print("Parent 2 Class")
#
# class child1(Parent1,Parent2):
#     def d3(self):
#         print("Child 1 Class")
# class child2(Parent1,Parent2):
#     def d4(self):
#         print("Child 2 Class")
# c1=child1()
# c2=child2()
# c1.d1()
# c1.d2()
# c1.d3()
# c2.d1()
# c2.d2()
# c2.d4()

class value1:
    a =int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    c = int(input("Enter c value: "))
class value2:
    d=int(input("Enter d value: "))

class add(value1,value2):
    @staticmethod
    def ad():
        print(value1.a+value2.d+value1.b+value1.c)
class sub(value1,value2):
    @classmethod
    def sb(cls):
        print(cls.a-cls.d,cls.b-cls.c)

c1=add()
c2=sub()
c1.ad()
c2.sb()