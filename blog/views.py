from django.shortcuts import render, redirect, get_object_or_404
from .models import Entrada

# Vista para listar las entradas
def lista_entradas(request):
    entradas = Entrada.objects.all().order_by('-fecha_creacion')  # Todas las entradas ordenadas por fecha
    return render(request, 'blog/lista.html', {'entradas': entradas})

# Vista para crear una nueva entrada
def crear_entrada(request):
    if request.method == 'POST':  # Solo procesamos datos si el método es POST
        title = request.POST.get('title')  # Capturamos el título desde el formulario
        subtitle = request.POST.get('subtitle')  # Capturamos el subtítulo desde el formulario
        descripcion = request.POST.get('descripcion')  # Capturamos la descripción desde el formulario

        # Creamos una nueva entrada en la base de datos
        Entrada.objects.create(
            title=title,
            subtitle=subtitle,
            descripcion=descripcion
        )

        # Redirigimos al listado de entradas
        return redirect('lista_entradas')

    return render(request, 'blog/blog.html')  # Renderizamos la plantilla del formulario si el método no es POST



def borrar(request, entrada_id):
    
    if request.method == 'POST':

        entrada = get_object_or_404(Entrada, id=entrada_id)

        entrada.delete()


        return redirect ('lista_entradas')