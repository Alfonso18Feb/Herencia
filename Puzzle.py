class Base: 
 
    def __init__(self): 
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
 
    def A(self): 
        print(self.a) #imprime a
 
    def B(self): 
        print(self.b)#imprime b
 
    def C(self): 
        print(self.c) #imprime c
 
class Derivada(Base): 
 
    def __init__(self): 
        self.a = "a" 
        super().__init__() 
        self.c = "cc" 
 
    def A(self): 
        print(self.a) #imprime aa
 
    def B(self): 
        self.b = "bb" 
        super().B() 
        print(self.b) #imprime 2*bb
 
base = Base() 
derivada = Derivada() 
 
base.A() #a
derivada.A()#a porque coje la seper.__innit de la base 
print() #espacio
base.B() #b
derivada.B()#2*bb\n 
base.C() #c
derivada.C()#cc 
derivada = base#ahora cambiamos de class 
derivada.C() #=base.C=c