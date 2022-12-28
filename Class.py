class product:
    id=101
    abc="hello"
    #instance method
    # def details(self,name,age):
    #     self.n=name
    #     self.a=age
    #     print(self.n,self.a)
    # #constructor
    # def __init__(self):
    #     print("default"
    #class method
    @classmethod
    def show(cls):
        cls.na=id
        cls.age=abc
        print(cls.na,cls.age)
product.show()