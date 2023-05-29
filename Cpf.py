class Cpf:
    def __init__(self, documento) -> None:
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
            self.cpf = self.formata_cpf()
        else:
            raise ValueError("CPF inválido!!!")
        
    def cpf_eh_valido(self, documento):
        return True if len(documento) == 11 else False
    
    def formata_cpf(self):
        cpf = self.cpf
        return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    
    def __str__(self) -> str:
        return self.cpf