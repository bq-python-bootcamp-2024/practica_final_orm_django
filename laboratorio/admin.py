from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto


class LaboratorioAdmin(admin.ModelAdmin):
    # Mostrar los siguientes campos
    list_display = ['id', 'nombre']

# Registrar modelo Laboratorio y su vista en sitio administrativo
admin.site.register(Laboratorio, LaboratorioAdmin)


class DirectorGeneralAdmin(admin.ModelAdmin):
    # Mostrar los siguientes campos
    list_display = ['id', 'nombre', 'laboratorio']

# Registrar modelo DirectorGeneral y su vista en sitio administrativo
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)


class ProductoAdmin(admin.ModelAdmin):
    # Mostrar los siguientes campos
    list_display = ['id', 'nombre', 'f_fabricacion', 'p_costo', 'p_venta']

    # Permitir filtro por nombre y laboratorio
    list_filter = ['nombre', 'laboratorio']

# Registrar modelo Producto y su vista en sitio administrativo
admin.site.register(Producto, ProductoAdmin)
