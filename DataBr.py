from datetime import datetime


class DataBr:
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()

    def get_mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março", "Abril",
            "Maio", "Junho", "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        indice_mes = self.momento_cadastro.month
        return meses_do_ano[indice_mes - 1]

    def get_dia_semana(self):
        dias_da_semana = [
            "Segunda", "Terça", "Quarta", "Quinta",
            "Sexta", "Sábado", "Domingo"
        ]
        indice_dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[indice_dia_semana]

    def __str__(self) -> str:
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
