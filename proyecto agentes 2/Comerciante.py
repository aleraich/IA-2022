# coding=utf-8
from Agricultor import *
from Comprador import *

class AgenteComerciante:


    def __init__(self):
        self.stock = 0
        self.pedidoActivado = False

    def vender(self,comprador):
        stockRequerido = comprador.comprar()
        if ('requiero' in stockRequerido) and (('zanahoria' in stockRequerido) or ('zanahorias' in stockRequerido)):
                    numeros = [int(temp)for temp in stockRequerido.split() if temp.isdigit()]
                    numero = self.unirnumeros(numeros)
                    if numero == 0:
                         print('Comerciante: no entiendo')
                    else:
                        if numero <= self.stock:
                            print('Comerciante: Le entrego su pedido')
                            respuesta = 'Entregar pedido'
                            comprador.aniadirzanahorias(numero)
                            comprador.agradecer()
                            self.reducirStock(numero)
                            return respuesta
                        else:
                            print('Comerciante: No tengo la cantidad que pide, hare pedido')
                            respuesta = 'No tengo la cantidad que requiere, hare pedido'
                            self.pedidoActivado = True
                        
        else:
            print('Comerciante: No entiendo')
            respuesta = 'No entiendo'
            return respuesta
    
    def pedir(self):
        pedido = input('Comerciante: ')
        return pedido    
    
    def getStock(self):
        return self.stock
        
    def agradecer(self):
        print('Comerciante: Gracias')

    def llenarStock(self,numero):
        self.stock = self.stock + numero
    
    def reducirStock(self,numero):
        self.stock = self.stock-numero

    def cambiarPedido(self,valor):
        self.pedidoActivado = valor

    def pedido(self):
        return self.pedidoActivado

    def unirnumeros(self,numeros):
        a = 0
        for numero in numeros:
            a = a * 10 + numero
        return a
        