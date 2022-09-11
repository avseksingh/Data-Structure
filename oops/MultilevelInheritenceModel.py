# class A:
#     def f1(self):
#         print('f1 in A')
#
# class B(A):
#     def f1(self):
#         print('f1 in B')
#
#     def f1a(self):
#         A().f1()
# class C(B):
#     def f1b(self):
#         B().f1()
#     def f1(self):
#         print('f1 in C')
# o = C()
# o.f1()
# o.f1a()
# o.f1b()


class A:
    def f1(self):
        print('f1 in A')

class B(A):
    def f1(self):
        A().f1()
        print('f1 in B')

class C(B):

    def f1(self):
        B().f1()
        print('f1 in C')
o = C()
o.f1()
