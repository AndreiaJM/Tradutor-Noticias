import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.service.noticia_service import NoticiasService
from src.model.noticias_dto import Noticia

from src.testes.samples.input import noticias_input
from src.testes.samples.output import noticias_output


class TesteNoticiasService(TestCase):

    def setUp(self) -> None:
        self.noticias_input = noticias_input
        self.noticias_output = noticias_output


    @patch('src.service.noticia_service.requests')
    def test_execute_traduzir_noticias_sucesso(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.noticias_input

        mock_requests.get.return_value = mock_response

        noticia_service = NoticiasService()

        get_noticias = noticia_service.buscar_noticias()

        Noticia(get_noticias)

        self.assertEqual(noticia_service.execute(),self.noticias_output)

    @patch('src.service.noticia_service.requests')
    def test_execute_traduzir_noticias_falha(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = self.noticias_input

        mock_requests.get.return_value = mock_response

        noticia_service = NoticiasService()

        self.assertEqual(noticia_service.execute(),{"mensagem": "Tente novamente mais tarde"})


if __name__=='__main__':
    unittest.main()