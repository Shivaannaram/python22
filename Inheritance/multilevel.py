# class Grandparent:
#     def d1(self):
#         print("Grand parent class")
#
# class parent(Grandparent):
#     def d2(self):
#         print("Parent Class")
# class child(parent):
#     def d3(self):
#         print("child class")
#
# c=child()
# c.d1()
# c.d2()
# c.d3()
class Product:
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    @staticmethod
    def d1():
        return Product.a*Product.b
class sum(Product):
    @classmethod
    def d2(cls):
        return cls.a+cls.b
s=sum()
print(s.d1())
print(s.d2())

