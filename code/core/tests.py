from django.test import TestCase
from django.shortcuts import resolve_url as r
from http import HTTPStatus
from pymongo import MongoClient

class IndexGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_found_html(self):
        tags = (
            ('<html>', 1),
            ('<body>', 1),
            ('<div>', 7),
            ('<section>', 1),
            ('<img>', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class CadastroGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:cadastro'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_found_html(self):
        tags = (
            ('<html>', 1),
            ('<body>', 1),
            ('<div>', 14),
            ('<input>', 6),
            ('<form>', 1),
            ('<fieldset>', 1)
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class EmpresaGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:empresa'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'empresa.html')

    def test_found_html(self):
        tags = (
            ('<html>', 1),
            ('<body>', 1),
            ('<div>', 14),
            ('<input>', 6),
            ('<form>', 1),
            ('<fieldset>', 1)
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class LoginGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:login'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'login.html')

    def test_found_html(self):
        tags = (
            ('<html>', 1),
            ('<body>', 1),
            ('<div>', 13),
            ('<input>', 6),
            ('<form>', 1),
            ('<button>', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class TicketGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:ticket'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'ticket.html')

    def test_found_html(self):
        tags = (
            ('<html>', 1),
            ('<body>', 1),
            ('<div>', 7),
            ('<section>', 3),
            ('<img>', 2),
            ('<p>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class MaterialGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:material'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'material.html')

    def test_found_html(self):
        tags = (
            ('<html>', 1),
            ('<body>', 1),
            ('<div>', 7),
            ('<section>', 3),
            ('<img>', 3),
            ('<p>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class greentradeModelsTest(TestCase):
    def test_criar_usuario(self):
        client = MongoClient("mongodb://localhost:27017")
        db = client['greentrade']
        collection = db['clientes']

        # Cria um documento no MongoDB
        cadastro_data = {'nome': 'Lucas'}
        result = collection.insert_one(cadastro_data)
        self.assertIsNotNone(result.inserted_id)

    def test_se_foi_criado(self):
    # Verifica se o documento existe no MongoDB
        client = MongoClient("mongodb://localhost:27017/greentrade")
        collection = client['greentrade']['clientes']
        documents = collection.find()
        self.assertTrue(documents.count() > 0)

    def test_criado_somente_um(self):
        # Verifica se apenas um documento foi criado
        client = MongoClient("mongodb://localhost:27017/greentrade")
        collection = client['greentrade']['clientes']
        documents = collection.find()
        self.assertEqual(documents.count(), 1)
