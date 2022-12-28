# class Parent1:
#     def d1(self):
#         print("parent 1")
# class Parent2:
#     def d2(self):
#         print("parent 2")
# class Parent3:
#     def d3(self):
#         print("parent 3")
# class child(Parent1,Parent2,Parent3):
#     def d4(self):
#         print("child ")
# c=child()
# c.d1()
# c.d2()
# c.d3()
# c.d4()
class parent1:
    a=10
    b=20
class parent2:
    c=20
    d=20
    e=c/d
class child(parent1,parent2):
    @staticmethod
    def d():
        print(parent1.a+parent1.b,parent2.c*parent2.d,parent2.e)
c=child()
c.d()