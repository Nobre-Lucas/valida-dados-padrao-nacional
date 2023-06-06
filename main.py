from Cpf import Cpf
from Cnpj import Cnpj
from TelefoneBr import TelefoneBr
from DataBr import DataBr

if __name__ == "__main__":
    cpf = Cpf("012.345.678-90")
    cnpj = Cnpj("35551316000156")
    telefone = TelefoneBr("55 91983746262")
    cadastro = DataBr()
    print(f"cpf: {cpf}")
    print(f"cnpj: {cnpj}")
    print(f"telefone: {telefone}")
    print(f"data de cadastro: {cadastro}")
    print(f"mês de cadastro: {cadastro.get_mes_cadastro()}")
    print(f"dia da semana de cadastro: {cadastro.get_dia_semana()}")
    