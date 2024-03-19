class A():
    def __init__(self,a):
        self.a=a
    def get_a(self):
        return self.a
def main():
    pass
if __name__=='__main__':
    main()

class B(A):
    def __init__(self,a,b):
        A().__init__(self, a)
        self.b=b
        self.a=a
    def get_b(self):
        return self.b
def main():
    pass
class C(A):
    def __init__(self,c,a):
        A().__init__(a)
        self.c=c
        self.a=a
    def get_c(self):
        return self.c
def main():
    pass

class D(B ,C):
    def __init__(self,a,b,c):
        C().__init__(self,a,c)
        B().__init__(self,a,b)
        self.a = a
        self.b = b
        self.c = c
    def get_d(self):
        return self.d
    def __str__():
        pass
def main():
    d = D(1, 2, 3)
    print(isinstance(d, B), isinstance(d, C),isinstance(d,A)) 
    print(D.a, D.b, D.c) 


