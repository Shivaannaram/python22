#Single Level
# class parent:
#     def d(self):
#         print("parent class")
# class child(parent):
#     def d1(self):
#         print("Child Class")
# c=child()
# c.d()
# c.d1()
class values:

    @classmethod
    def d(cls,a,b):
        cls.a=a
        cls.b=b
        print(cls.a-cls.b)
class add(values):
    def x(self,a,b):
        print(a+b)

a=add()
a.d(10,11)
a.x(10,11)
