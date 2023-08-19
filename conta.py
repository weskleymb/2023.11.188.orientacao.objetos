class Conta:

    # atributos
    __agencia: int
    __numero: int
    __titular: str
    __saldo = 0.0

    # construtor
    def __init__(self, agencia: int, numero: int, titular: str):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
    
    # propriedades
    @property
    def agencia(self) -> int:
        return self.__agencia
    
    @property
    def numero(self) -> int:
        return self.__numero
    
    @property
    def titular(self) -> str:
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    @property
    def saldo(self) -> float:
        return self.__saldo
    
    # metodos
    def depositar(self, valor: float):
        pode_depositar = valor > 0
        if pode_depositar:
            self.__saldo += valor

    def sacar(self, valor: float):
        pode_sacar = valor > 0 and self.__saldo >= valor
        if pode_sacar:
            self.__saldo -= valor

    # criar o metodo de transferir
    def transferir(self, valor: float, conta_destino):
        pode_transferir = valor > 0 and self.__saldo >= valor
        if pode_transferir:
            self.sacar(valor)
            conta_destino.depositar(valor)
