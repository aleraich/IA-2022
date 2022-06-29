# coding=utf-8
from Agricultor import *
from Comerciante import *
from Comprador import *

class Interaccion:

    def __init__(self,comerciante,agricultor,comprador):
        self.comerciante = comerciante
        self.agricultor = agricultor
        self.comprador = comprador

        while True:
            if comerciante.pedido() == True:
                agricultor.entregarAComerciante(comerciante)
                if agricultor.pedido() == False:
                    comerciante.cambiarPedido(False)
            else:
                comerciante.vender(comprador)

comerciante = AgenteComerciante()
agricultor = AgenteAgricultor()
comprador = AgenteComprador()
interactor = Interaccion(comerciante, agricultor,comprador)