from django.test import TestCase

# Create your tests here.

from http import HTTPStatus
from unittest import result
from django.test import TestCase

from projetoferiado.core.FeriadosAPI import FeriadosAPI

# Create your tests here.
class FormTest(TestCase):
    def setUp(self):
        self.mockedData = {'nome': 'teste', 'data': '2022-07-02'}
    def testPost(self):
        res = self.client.post('/cadastro/', dtaa=self.mockedData)

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertContains(res, 'Feriado inserido com sucesso')

class FeriadoApiTest(TestCase):
    def test_instanciar_objeto(self):
        objeto = FeriadosAPI(2022)
        assert objeto._ano, 2022
        assert type(objeto.feriados) == list
        assert len(objeto.feriados) == 11

    def test_str_repr(self):
        objeto = FeriadosAPI(2023)
        msg = 'Feriados de 2023'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_str_repr2(self):
        objeto = FeriadosAPI(2022)
        msg = 'Feriados de 2022'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_properties(self):
        objeto = FeriadosAPI(2022)
        assert objeto.ano == '2022'