from  src.model.noticias_dto import Noticia
from src.testes.samples.input import noticias_input

obj_noticia = Noticia(noticias_input)

a=obj_noticia.traduzir()
print(a)


