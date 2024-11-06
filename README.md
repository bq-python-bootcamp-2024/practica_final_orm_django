# Configuración proyecto practica final orm Django

## Descripción
Prototipo de sistema de administración de laboratorios fabricantes de medicamentos.

## Hitos de desarrollo
1. Se crea aplicación laboratorio que permite listar, insertar, actualizar y eliminar laboratorios.

## Instalación

1. Clonar el repositorio: `git clone https://github.com/bq-python-bootcamp-2024/practica_final_orm_django.git`

2. (Opcional) Crear entorno para el proyecto: [Crear entorno con `virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

3.  Instalar las dependencias listadas en ["requirements.txt"](requirements.txt): `python -m pip install -r requirements.txt`

2. Copiar archivo .env con información protegida en el directorio principal del proyecto (enviado a la plataforma).

3. Seguir instrucciones para configurar la base de datos (especificadas más abajo).

3. Realizar migraciones: `python manage.py migrate`

4. Crear un usuario administrador: `python manage.py createsuperuser`

5. Poner en marcha el servidor de prueba: `python manage.py runserver`
   
## Configuración base de datos PostgreSQL

### Crear una base de datos en PostgreSQL llamada db_final_orm con el usuario userdjango, que posea la contraseña 'userdjango'.

### Shell de PostgreSQL
```
postgres=# CREATE USER userdjango WITH PASSWORD 'userdjango';
CREATE ROLE
```

```
postgres=# CREATE DATABASE db_final_orm OWNER userdjango;
CREATE DATABASE
```

## Registro configuración inicial del proyecto
### Crear proyecto de django
```
practica_final_orm_django> django-admin startproject config .
```

### Crear superusuario admin con clave 'admin'
```
practica_final_orm_django> python ./manage.py createsuperuser
```

### Crear aplicación laboratorio
```
practica_final_orm_django> django-admin startapp laboratorio
```

## Consultas realizadas a la aplicación laboratorio

### Importar modelos Laboratorio, DirectorGeneral y Producto

```
from laboratorio.models import Laboratorio, DirectorGeneral, Producto
```

### Insertar los siguientes datos para replicar los resultados de las consultas a continuación
```
# Crear laboratorios
l1 = Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Santiago', pais='Chile')
l2 = Laboratorio.objects.create(nombre='Laboratorio 2', ciudad='Santiago', pais='Chile')
l3 = Laboratorio.objects.create(nombre='Laboratorio 3', ciudad='Santiago', pais='Chile')

# Crear Directores Generales y asignarles un laboratorio
d1 = DirectorGeneral.objects.create(nombre='Director General 1', laboratorio=l1, especialidad='Químico farmaceutico')
d1 = DirectorGeneral.objects.create(nombre='Director General 2', laboratorio=l2, especialidad='Químico farmaceutico')
d1 = DirectorGeneral.objects.create(nombre='Director General 3', laboratorio=l3, especialidad='Químico farmaceutico')

# Crear un producto por laboratorio
p1 = Producto.objects.create(nombre='Producto 1', laboratorio=l1, f_fabricacion=2022, p_costo=1500, p_venta=2000)
p2 = Producto.objects.create(nombre='Producto 2', laboratorio=l2, f_fabricacion=2021, p_costo=2500, p_venta=3000)
p3 = Producto.objects.create(nombre='Producto 3', laboratorio=l3, f_fabricacion=2019, p_costo=3500, p_venta=4000)

```

### 1. Obtenga todos los objetos tanto Laboratorio, DirectorGeneral y Productos.
```
laboratorios_totales = Laboratorio.objects.all()
directores_generales_totales = DirectorGeneral.objects.all()
productos_totales = Producto.objects.all()
```
### 2. Obtenga el laboratorio del Producto cuyo nombre es ‘Producto 1’.
```
productos_filtrados = productos_totales.filter(nombre='Producto 1')
if len(productos_filtrados) > 0:
    laboratorio_producto_1 = productos_filtrados[0].laboratorio
```
```
# Output:
Laboratorio 1
```
### 3. Ordene todos los productos por nombre, y que muestre los valores de nombre y laboratorio.
```
productos_ordenados = productos_totales.order_by('nombre')
for p in productos_ordenados:
    print(f'Nombre producto: {p.nombre}, Nombre laboratorio: {p.laboratorio.nombre}')
```
```
# Output:
Nombre producto: Producto 1, Nombre laboratorio: Laboratorio 1
Nombre producto: Producto 2, Nombre laboratorio: Laboratorio 2
Nombre producto: Producto 3, Nombre laboratorio: Laboratorio 3
```
### 4. Realice una consulta que imprima por pantalla los laboratorios de todos los productos.
```
for p in productos_totales:
    print(f'Nombre laboratorio: {p.laboratorio.nombre}')
```
```
# Output:
Nombre laboratorio: Laboratorio 1
Nombre laboratorio: Laboratorio 2
Nombre laboratorio: Laboratorio 3
```