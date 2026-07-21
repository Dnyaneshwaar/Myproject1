
# multiple inheritance possible in python

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

    def m4(self,p,q):
        print(p+q)

class B:
    a,b=200,100
    def m2(self):
        print(self.a-self.b)

class C(A,B):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)


cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()
cobj.m4(7,8)