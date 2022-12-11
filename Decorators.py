un=input("Enter username: ")
pw=input("Enter password: ")
def d1(fun):
    def d2(un,pw):
        if (un == "a" and pw == "A"):
            return "Login Success"
        else:
            return "Login failed"
    return d2

def d3(un,pw):
    return un,pw
d=d1(d3)
print(d(un,pw))