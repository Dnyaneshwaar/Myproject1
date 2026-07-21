# creating class with object  * Self is representing the class

# class Myclass:
#     def myfun(self):
#         pass
#     def display(selfself,name):
#         print(name)
#
# mc1 = Myclass()
# mc1.myfun()
# mc1.display("john")
#
# mc2 = Myclass()
# mc2.display("jack")

# static method

# 'Self' inside the static method just represent parameter, it's doesn't refer object & class as like normal function/method

# class Myclass:
#     def m1(self):
#         print("this is instance method")
#
#     @staticmethod
#     def m2(self,num):  # 2 parameter
#         print(self,num)
#
# mc = Myclass()
# mc.m1()
# mc.m2(10,2 )

# Myclass.m2(7,5)

# defining variables

# class Myclass:
#     a,b=10,20  # class variables.
#
#     def add(self):
#         print(self.a+self.b)  # to access class variables in method. Self should use
#
# mc = Myclass()
# mc.add()


# local variables, Global variables & class variables
#
# i,j=4,5  # global variable
#
# class Myclass:
#     p,q=10,20  # class variables
#     def add(self,x,y):  # local variables
#         print(x*y)
#         print(i*j)
#         print(self.p+self.q)
#
# co1 = Myclass()
# co1.add(40,50)

# A class with constructor & method

class Myemployee:

    def __init__(self,eid,name,sal):
        self.eid=eid
        self.name=name
        self.sal=sal

    def display(self):
        print(self.eid,self.name,self.sal)

e1 = Myemployee(101,"john","6000000")
e1.display()
e2=Myemployee(102,"jack","9000000")
e2.display()



