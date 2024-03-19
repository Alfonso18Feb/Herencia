



class puntos2D():
    def __init__(self,x,y,a,b):
        self.x=x
        self.y=y
        self.a=a
        self.b=b
    def get_x(self):
        if isinstance(self.x,float):
            return self.x
        else:
            raise TypeError('No es un numero float')
    def get_y(self):
        if isinstance(self.y,float):
            return self.y
        else:
            raise TypeError('No es un numero float')
    def get_a(self):
        if isinstance(self.a,float):
            return self.a
        else:
            raise TypeError('No es un numero float')
    def get_b(self):
        if isinstance(self.b,float):
            return self.b
        else:
            raise TypeError('No es un numero float')
    def translacion2D(self,a,b):
        self.x+=a 
        self.y+=b
        
    def __str__(self,a,b):
        return "X:{}; Y: {}".format(self.x, self.y)
        
def main():
    q=input('cual es el valor x:')
    w=input('cual es el valor y:')
    e=input('cual es el nuevo punto a:')
    r=input('cual es el nuevo punto b:')
    funcion=puntos2D(q,w,e,r)
    sad=funcion.translacion2D
    print(sad)
if __name__=='__main__':
    main()


        