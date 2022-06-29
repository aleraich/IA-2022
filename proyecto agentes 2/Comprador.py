# coding=utf-8

from Comerciante import *

class AgenteComprador:

    def __init__(self):
        self.canastaDeZanahorias = 0

    def comprar(self):
        pedido = input('Comprador: ')
        return pedido

    def agradecer(self):
        print('Comprador: Gracias')

    def aniadirzanahorias(self,numero):
        self.canastaDeZanahorias = self.canastaDeZanahorias + numero


