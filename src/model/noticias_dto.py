import json

from src.model.dados_noticia_dto import DadosNoticia
from deep_translator import GoogleTranslator

traduzir = GoogleTranslator(source='auto', target='pt')

class Noticia:

    categoria: str
    dados: list

    def __init__(self, api_noticias: dict):
        dados = DadosNoticia()

        self.categoria = api_noticias['category']
        self.dados = dados.dados_api(api_noticias)

    def traduzir(self):
        lista = []
        json_list = {}

        try:
            categoria = traduzir.translate(self.categoria)

            for dados in self.dados:

                autor = dados['author']
                titulo = traduzir.translate(dados['title'])
                conteudo = traduzir.translate(dados['content'])
                data = dados['date']
                fonte = dados['readMoreUrl']

                lista.append({
                    "autor": autor,
                    "titulo": titulo,
                    "conteudo": conteudo,
                    "data": data,
                    "fonte": fonte
                })

            json_list.update({"categoria": categoria})
            json_list.update({"dados": lista})

            return json_list

        except:

            return {"Mensagem": "Nao é possivel traduzir, tente novamente mais tarde"}








