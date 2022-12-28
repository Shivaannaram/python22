# class Parent:
#     def d1(self):
#         print("Parent Method")
#
# class child1(Parent):
#     def d2(self):
#         print("Child1 Method")
# class child2(Parent):
#     def d3(self):
#         print("child2 method")
# c1=child1()
# c2=child2()
# c1.d1()
# c1.d2()
# c2.d1()
# c2.d3()
class Parent:
    a=int(input("Enter a value:"))
    b = int(input("Enter a value:"))
class child(Parent):
    @staticmethod
    def d():
        print(Parent.a+Parent.b)
class child2(Parent):
    @classmethod
    def d1(cls):
        print(cls.a-cls.b)
c1=child()
c2=child2()
c1.d()
c2.d1()