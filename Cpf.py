from validate_docbr import CPF

class Cpf:
    def __init__(self, documento) -> None:
        documento = str(documento)
        if len(documento) != 11 and len(documento) != 14:
            raise ValueError("Quantidade de dígitos deve ser 11")
        if not self.cpf_eh_valido(documento):
            raise ValueError("CPF inválido!!!")
        else:
            self.cpf = documento
            self.formata_cpf()
        
    def cpf_eh_valido(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def formata_cpf(self):
        if len(self.cpf) == 11:
            mascara = CPF()
            self.cpf = mascara.mask(self.cpf)
    
    def __str__(self) -> str:
        return self.cpf