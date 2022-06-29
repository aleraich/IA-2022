# coding=utf-8

from Comerciante import *

class AgenteAgricultor:


    def __init__(self):
        self.cultivo = 0
        self.cosecha = 0
        self.pedidoActivado = True

    def cultivar(self):
        self.cultivo = self.cultivo + 20

    def cosechar(self):
        if (self.cultivo-10 > 0):
           self.cosecha = self.cosecha + 10
           self.cultivo = self.cultivo - 10
        else:
            self.cultivar()
    
    def entregarAComerciante(self,comerciante):
        print('Agricultor: requiere cargas de zanahoria?')
        pedido = comerciante.pedir()
        if pedido == 'no requiero cargas':
            print('Agricultor: esta bien, gracias')
            self.pedidoActivado = False
        else:
            if ('requiero' in pedido) and (('cargas' in pedido) or ('carga' in pedido)):
                    numeros = [int(temp)for temp in pedido.split() if temp.isdigit()]
                    numero = self.unirnumeros(numeros)
                    if numero == 0:
                         print('Agricultor: no entiendo')
                         respuesta = 'No entiendo'
                         return respuesta
                    else:
                        if numero <= self.cosecha:
                            print('Agricultor: Le entrego pedido')
                            respuesta = 'Entregar pedido'
                            comerciante.agradecer()
                            comerciante.llenarStock(numero*20)
                            return respuesta
                        else:
                            print('Agricultor: No tengo la cantidad de pedido, ire a cultivar')
                            respuesta = 'No tengo la cantidad de pedido, ire a cultivar'
                            self.cultivar()
                            self.cosechar()
                            return respuesta
                        
            else:
                print('Agricultor: No entiendo')
                respuesta = 'No entiendo'
                return respuesta
    
    def pedido(self):
        return self.pedidoActivado

    def unirnumeros(self,numeros):
        a = 0
        for numero in numeros:
            a = a * 10 + numero
        return a
        



