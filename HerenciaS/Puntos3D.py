



from PUNTOS2D import *

class puntos3D(puntos2D):
    def __init__(self,z,c):
        puntos2D().__init__()#constructor del padre
        #añadimos variabes nuevas de esta clase
        self.z=z
        self.c=c
    #Los getters de las nuevas varianles
    def get_z(self):
        if isinstance(self.z,float):
            return self.z
        else:
            raise TypeError('No has escrito un float')
    def get_c(self):
        if isinstance(self.c,float):
            return self.c
        else:
            raise TypeError('No has escrito un float')
    def translacion3D(self,a,b,c):
        super().translacion2D(a,b)#añadimos las translacion de el padre
        self.z+=c#propedad de 3D
    def __str__(self):
        return super().__str__()+";Z :{}".format(self.z)
def main():
    was=puntos3D(1,2,3)
    saw=was.translacion3D
    print(saw)

