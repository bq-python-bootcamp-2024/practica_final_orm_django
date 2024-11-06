from django.test import TestCase
from django.urls import reverse

# Modelos aplicación laboratorio
from .models import Laboratorio

# Modelo para pruebas unitarias de la aplicación laboratorio
# Incluye revisión de todas las url disponibles para las operaciónes CRUD
# No incluye pruebas al método POST, solo GET.
class LaboratorioTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            id=1,
            nombre='Laboratorio de prueba',
            ciudad='Santiago', pais='Chile'
        )
    
    def test_modelo_laboratorio(self):
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio de prueba')
        self.assertEqual(self.laboratorio.ciudad, 'Santiago')
        self.assertEqual(self.laboratorio.pais, 'Chile')
    
    def test_existe_url_laboratorio_listar(self):
        response = self.client.get('/laboratorio/listar/')
        self.assertEqual(response.status_code, 200)
    
    def test_existe_url_laboratorio_insertar(self):
        response = self.client.get('/laboratorio/insertar/')
        self.assertEqual(response.status_code, 200)
    
    def test_existe_url_laboratorio_actualizar(self):
        response = self.client.get('/laboratorio/1/actualizar/')
        self.assertEqual(response.status_code, 200)

    def test_existe_url_laboratorio_eliminar(self):
        response = self.client.get('/laboratorio/1/eliminar/')
        self.assertEqual(response.status_code, 200)

    def test_pagina_laboratorio_listar(self):
        response = self.client.get(reverse('listar_laboratorio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_laboratorio.html")
        self.assertContains(response, "Información de Laboratorios")
    
    def test_pagina_laboratorio_insertar(self):
        # response = self.client.get('/laboratorio/insertar/')
        response = self.client.get(reverse('insertar_laboratorio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "formulario_laboratorio.html")
        self.assertContains(response, "Insertar los datos del laboratorio")

    def test_pagina_laboratorio_actualizar(self):
        response = self.client.get(reverse('actualizar_laboratorio', kwargs={'id_laboratorio': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "formulario_laboratorio.html")
        self.assertContains(response, "Actualizar laboratorio")

    def test_pagina_laboratorio_eliminar(self):
        response = self.client.get(reverse('eliminar_laboratorio', kwargs={'id_laboratorio': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "eliminar_laboratorio.html")
        self.assertContains(response, "Estas seguro que deseas eliminar el laboratorio")
