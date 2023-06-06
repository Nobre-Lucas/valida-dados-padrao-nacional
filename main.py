from Cpf import Cpf
from Cnpj import Cnpj
from TelefoneBr import TelefoneBr

if __name__ == "__main__":
    cpf = Cpf("012.345.678-90")
    cnpj = Cnpj("35551316000156")
    telefone = TelefoneBr("55 91983746262")
    print(f"cpf: {cpf}")
    print(f"cnpj: {cnpj}")
    print(f"telefone: {telefone}")
    