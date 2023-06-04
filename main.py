from src.service.noticia_service import Noticia
import requests

URL = 'https://inshorts.deta.dev/news?category=science'

class Main:

    def executar_proj(self):
        retorno_api = requests.get(URL)

        if retorno_api.status_code == 200:
            retorno_api = retorno_api.json()
        else:
            return  {"mensagem": "Erro no sevidor"}

        noticia=Noticia(retorno_api)

        return noticia.traduzir()

main = Main()

print(main.executar_proj())








