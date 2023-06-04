from src.model.noticias_dto import Noticia
from src.server.instance import server
from src.service.noticia_service import NoticiasService

app, api = server.app, server.app

@api.route('/noticias')
#class BuscaNoticias(Resource): #Resource é reponsavel pelos metodos http
def get():
    obj = NoticiasService()
    result = obj.execute()
    return result






