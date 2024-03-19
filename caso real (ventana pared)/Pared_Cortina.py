
from Pared_ventana import pared_ventana


class pared_cortina(pared_ventana):
    def __init__(self,paredcortina,pared,ventana):
        super().__init__(pared,ventana)
        self.paredcortina=paredcortina
    def get_paredcortina(self):
        return self.paredcortina
    def set_paredcortina(self,paredcortina):
        self.pared[0]=paredcortina
    def pared_A_cristal(self,paredcortina):
        self.ventana=paredcortina
        if self.ventana.key()==paredcortina:
            return self.ventana
        else: 
            raise TypeError('Error 2 no se esta relacionando la pared con una ventana mas grande')
def main():
    pared_ventana().__main__()
    result = pared_cortina.pared_ventana.superficie_acristalada()
    print(result)
if __name__=='__main__':
    main()