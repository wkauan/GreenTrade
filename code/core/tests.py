from django.test import TestCase
from pymongo import MongoClient

class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    #Este erro indica que o recurso que você está tentando acessar não foi encontrado.
    def test_200(self):
        self.assertEqual(200, self.resp.status_code)
    
class odsModelsTest(TestCase):

    def test_criar_usuario(self):
        client = MongoClient("mongodb://localhost:27017")
        db = client['odsdatabase']
        collection = db['odscliente']

        # Cria um documento no MongoDB
        cadastro_data = {'nome': 'Bolsonaro'}
        result = collection.insert_one(cadastro_data)
        self.assertIsNotNone(result.inserted_id)

    def test_se_foi_criado(self):
    # Verifica se o documento existe no MongoDB
        client = MongoClient("mongodb://localhost:27017/odsdatabase")
        collection = client['odsdatabase']['odscliente']
        documents = collection.find()
        self.assertTrue(documents.count() > 0)

    def test_criado_somente_um(self):
        # Verifica se apenas um documento foi criado
        client = MongoClient("mongodb://localhost:27017/odsdatabase")
        collection = client['odsdatabase']['odscliente']
        documents = collection.find()
        self.assertEqual(documents.count(), 1)