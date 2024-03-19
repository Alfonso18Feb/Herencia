
class pared_ventana():
    '''constructor de la clase padre de pared_ventana y sus atributos
    pared es una lista y ventana es un dictionario'''
    def __init__(self,pared,ventana):
        self.pared=pared
        self.ventana=ventana
    '''Los getters a todos los atributos y un setter a las ventanas porque 
    la superficie que son los values pueden cambiar'''
    def get_pared(self):
        return self.pared
    def get_ventana(self):
        return self.ventana
    def set_ventana(self,ventana):
        self.ventana=ventana
    '''La siguiente funcion crea una lista de los valores(superficie) de las ventanas y las suma'''
    def superficie_acristalada(self,):
        r = self.ventana.values()
        suma_superficie=sum(r)
        return suma_superficie
'''El main es muy interactivo ya que puedes elegir la superficie que deseas y el progrma te lo sumaria'''
def main():
    pared=['pared_norte','pared_sur', 'pared_oeste', 'pared_este']
    n=float(input('sup_ven_norte:'))
    s=float(input('sup_ven_sur:'))
    o=float(input('sup_ven_oeste:'))
    e=float(input('sup_ven_este:'))
    ventana={'ventana_norte':n,'ventana_sur':s, 'ventana_oeste':o, 'ventana_este':e}
    p=pared_ventana(pared,ventana)
    result = p.superficie_acristalada()
    print(result)
if __name__=='__main__':
    main()