import re

class TelefoneBr:
    def __init__(self, telefone) -> None:
        if self.valida_telefone(telefone):
            self.telefone = self.formata_numero(telefone)
        else:
            raise ValueError("Número Incorreto")
    
    def valida_telefone(self, telefone) -> bool:
        padrao = "(\d{2,3})?(\d{2})(\d{4,5})(\d{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False
        
    def formata_numero(self, numero):
        padrao = "(\d{2,3})? (\d{2})(\d{4,5})(\d{4})"
        resposta = re.search(padrao, numero)
        numero_formatado = f"+{resposta.group(1)} ({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        return numero_formatado
        
    def __str__(self) -> str:
        return self.telefone
            