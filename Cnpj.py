from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento) -> None:
        documento = str(documento)
        if len(documento) != 14 and len(documento) != 18:
            raise ValueError("Quantidade de dígitos deve ser 14")
        if not self.cnpj_eh_valido(documento):
            raise ValueError("CNPJ inválido!!!")
        else:
            self.cnpj = documento
            self.formata_cnpj()
        
    def cnpj_eh_valido(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def formata_cnpj(self):
        if len(self.cnpj) == 14:
            mascara = CNPJ()
            self.cnpj = mascara.mask(self.cnpj)
    
    def __str__(self) -> str:
        return self.cnpj