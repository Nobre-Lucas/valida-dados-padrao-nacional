import requests


class Cep:

    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido!")

    def cep_e_valido(self, cep):
        return True if len(cep) == 8 else False

    def formata_cep(self, cep):
        return f"{cep[:5]}-{cep[5:]}"

    def acessa_api_viacep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json"
        request = requests.get(url)
        dados = request.json()
        return (
            f"bairro: {dados['bairro']}",
            f"cidade: {dados['localidade']}",
            f"UF: {dados['uf']}"
        )

    def __str__(self) -> str:
        return self.formata_cep(self.cep)
