import datetime
from django.core.exceptions import ValidationError
from django.db import models

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    # Migración 'actualizado_campos'
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'laboratorio'
        verbose_name_plural = 'laboratorios'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    # Migración 'actualizado_campos'
    especialidad = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Director General'
        verbose_name_plural = 'Directores Generales'
        ordering = ['id']

    def __str__(self):
        return self.nombre

# Funciones utilizadas en la validación del modelo producto
# Función para validar que el año sea posterior a 2015
def validar_anno(anno):
    if anno < 2015:
        raise ValidationError(f'La fecha de fabricación debe ser igual o posterior al año 2015.')

# Función para obtener el año actual
def anno_actual():
    return datetime.datetime.now().year

class Producto(models.Model):
    # Definir límite para fecha de fabricación y crear opciónes disponibles
    MIN_ANNO = 2015
    OPCIONES_ANNO = [(i, i) for i in range(MIN_ANNO, datetime.datetime.now().year+1)]

    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.IntegerField(choices=OPCIONES_ANNO, validators=[validar_anno], default=anno_actual)
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['id']

    def __str__(self):
        return self.nombre