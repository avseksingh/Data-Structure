class A:
    def f(self):
        print("Class A method f")


class B(A):
    def f(self):
        print("Class B method fb")
        A.f(self)


objb = B()
obja = A()
objb.f()
