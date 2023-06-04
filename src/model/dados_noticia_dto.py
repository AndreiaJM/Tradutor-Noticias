class DadosNoticia:
    def __init__(self):

        self.autor: str
        self.titulo: str
        self.conteudo: str
        self.data: str
        self.fonte: str

    def dados_api(self, api_noticias: dict):

        lista = []

        for dado in api_noticias['data']:

            self.autor = dado['author']
            self.titulo = dado['title']
            self.conteudo = dado['content']
            self.data = dado['date']
            self.fonte = dado['readMoreUrl']

            lista.append(dado)

        return lista
