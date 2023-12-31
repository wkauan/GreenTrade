from django.test import TestCase
from django.shortcuts import resolve_url as r
from http import HTTPStatus

# Teste da página Index
class IndexGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body', 1),
            ('<div', 7),
            ('<section', 2),
            ('<img', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

# Teste da página Cadastro
class CadastroGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:cadastro'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body', 1),
            ('<div', 13),
            ('<input', 7),
            ('<form', 1),
            ('<fieldset', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

# Teste da página Cadastro de Empresa
class EmpresaGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:empresa'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'empresa.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body', 1),
            ('<div', 13),
            ('<input', 7),
            ('<form', 1),
            ('<fieldset', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

# Teste da página Login
class LoginGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:login'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'login.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body', 1),
            ('<div', 12),
            ('<input', 3),
            ('<form', 1),
            ('<button', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

# Teste da página Ticket
class TicketGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:ticket'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'ticket.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body', 1),
            ('<div', 6),
            ('<section', 2),
            ('<img', 2),
            ('<p', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

# Teste da página Material
class MaterialGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:material'), follow=True)
    
    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'material.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body', 1),
            ('<div', 6),
            ('<section', 3),
            ('<img', 3),
            ('<p', 4),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

# Teste da página Coleta
class ColetaGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:coleta'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code, HTTPStatus.OK)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'coleta.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body', 1),
            ('<div', 5),
            ('<ul', 1),
            ('<section', 1),
            ('<h1', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
        