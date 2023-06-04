import json

from src.model.noticias_dto import Noticia
from deep_translator import GoogleTranslator
import requests

URL = 'https://inshorts.deta.dev/news?category=science'
traduzir = GoogleTranslator(source='auto', target='pt')

class NoticiasService:

    def execute(self):
        api_noticias = self.buscar_noticias()

        if api_noticias.status_code == 200:
            resp = api_noticias.json()
            traducao = Noticia(resp)
            return traducao.traduzir()

        return {"mensagem": "Tente novamente mais tarde"}

    def buscar_noticias(self):
        api_noticias = requests.get(URL)
        return api_noticias
