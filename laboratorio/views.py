from django.shortcuts import render, redirect
from django.contrib import messages

# Modelos y formularios aplicación laboratorio
from .models import Laboratorio
from .forms import LaboratorioForm

# Redirigir al usuario a la vista principal de laboratorio
def index(request):
    return redirect('/laboratorio/listar')

# Vista principal de laboratorio
# Permite listar los laboratorios registrados en el sistema y
# permite a los usuarios acceder a las vistas para insertar, actualizar y eliminar un laboratorio
def listar_laboratorio(request):
    laboratorios = Laboratorio.objects.all()
    context = {
        'titulo_documento': 'Información de Laboratorios',
        'titulo': 'Información de Laboratorios',
        'laboratorios': laboratorios
    }
    return render(request, 'listar_laboratorio.html', context=context)

# CRUD: Vista insertar laboratorio
def insertar_laboratorio(request):
    # Método POST
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Se ha insertado exitosamente el laboratorio: {form.cleaned_data['nombre']}.')
        else:
            messages.error(request, 'El registro del laboratorio ha fallado. Verifique la información ingresada.')
            
        return redirect('/laboratorio/insertar')

    # Método GET
    elif request.method == 'GET':
        form = LaboratorioForm()
        context = {
            'titulo_documento': 'Insertar laboratorio',
            'titulo': 'Insertar los datos del laboratorio',
            'form': form,
        }
        return render(request, 'formulario_laboratorio.html', context=context)

# CRUD: Vsita actualizar laboratorio
# Requiere parámetro url id_laboratorio
def actualizar_laboratorio(request, id_laboratorio):
    # Verificar la existencia del laboratorio que se requiere actualizar
    try:
        laboratorio = Laboratorio.objects.get(id=id_laboratorio)
    except Laboratorio.DoesNotExist:
        # En caso de error se redirige a la página prinicipal
        messages.error(request, 'El laboratorio que busca no existe.')
        return redirect('/laboratorio/listar')

    # Método POST
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            messages.success(request, f'Se ha actualizado exitosamente el laboratorio: {form.cleaned_data['nombre']}.')
        else:
            messages.error(request, 'La actualización del laboratorio ha fallado. Verifique la información ingresada.')
            
        return redirect('/laboratorio/listar')

    # Método GET
    elif request.method == 'GET':
        form = LaboratorioForm(instance=laboratorio)
        context = {
            'titulo_documento': 'Actualizar laboratorio',
            'titulo': 'Actualizar laboratorio',
            'form': form,
        }
        return render(request, 'formulario_laboratorio.html', context=context)

# CRUD: Vsita eliminar laboratorio
# Requiere parámetro url id_laboratorio
def eliminar_laboratorio(request, id_laboratorio):
    # Verificar la existencia del laboratorio que se requiere actualizar
    try:
        laboratorio = Laboratorio.objects.get(id=id_laboratorio)
    except Laboratorio.DoesNotExist:
        # En caso de error se redirige a la página prinicipal
        messages.error(request, 'El laboratorio que busca no existe.')
        return redirect('/laboratorio/listar')

    # Método POST
    if request.method == 'POST':
        nombre = laboratorio.nombre
        laboratorio.delete()
        messages.success(request, f'Se ha eliminado exitosamente el laboratorio: {nombre}')
        return redirect('/laboratorio/listar')
    
    # Método GET
    elif request.method == 'GET':
        context = {
            'titulo_documento': 'Eliminar laboratorio',
            'nombre_laboratorio': laboratorio.nombre,
        }
        return render(request, 'eliminar_laboratorio.html', context=context)
