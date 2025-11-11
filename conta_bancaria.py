class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def extrato(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}"

if __name__ == "__main__":
    conta = ContaBancaria("Carlos", 500)
    conta.depositar(250)
    conta.sacar(100)
    print(conta.extrato())