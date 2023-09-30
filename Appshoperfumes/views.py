from django.shortcuts import render, render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin#BASADA EN CLASES
from django.contrib.auth.decorators import login_required  #BASADA EN FUNCIONES
from .models import Categoria, Cliente, Producto, Pedido, Avatar, Blog
from .forms import  AvatarFormulario, AgregaCategoriaFormulario, AgregaProductoFormulario, ClienteFormulario, UserRegisterForm, UserEditForm



class BlogList(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blog'

class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

class BlogCreate(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class BlogUpdate(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    success_url = '/app-shoperfumes/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class BlogDelete(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = '/app-shoperfumes/'





def categoria(req,nombre):
    categoria = Categoria(nombre=nombre)
    categoria.save()
    return HttpResponse (f""" <p>Categoria: {categoria.nombre}<p>""")

def lista_categorias(req):
    lista = Categoria.objects.all()
    return render(req, "lista_categorias.html", {"lista_categorias":lista})

def agregacategoria(req: HttpRequest):
    print('method', req.method)
    print('post', req.POST)
    if req.method == 'POST':
        miFormulariocategoria = AgregaCategoriaFormulario(req.POST)
        if miFormulariocategoria.is_valid():
            print(miFormulariocategoria.cleaned_data)
            data = miFormulariocategoria.cleaned_data
            categoria= Categoria(nombre=data["nombre"])
            categoria.save()
            return render(req, "inicio.html", {"mensaje": "Categoria creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})    
    else:
        miFormulariocategoria = AgregaCategoriaFormulario()
        return render(req, "agregacategoria.html", {"miFormulariocategoria": miFormulariocategoria})
    


def inicio(req):

    try:

        avatar = Avatar.objects.get(user=req.user.id)  #daba error y se le agrego una excepcion
        return render(req, "inicio.html", {"url": avatar.imagen.url})
    except:
        return render(req, "inicio.html")


def producto(req):
    return render(req, "produto.html")

def producto(req,nombre):
    producto = Producto(nombre=nombre)
    producto.save()
    return HttpResponse (f""" <p>Cliente: {producto.nombre}<p>""")

def lista_productos(req):
    lista = Producto.objects.all()
    return render(req, "producto.html", {"lista_productos":lista})


def agregarproducto(req: HttpRequest):
    print('method', req.method)
    print('post', req.POST)
    if req.method == 'POST':
        miFormularioproducto =  AgregaProductoFormulario(req.POST)
        if miFormularioproducto.is_valid():
            print(miFormularioproducto.cleaned_data)
            data = miFormularioproducto.cleaned_data
            producto = Producto(nombre=data["nombre"], precio=data["precio"])
            producto.save()
            return render(req, "inicio.html", {"mensaje": "Producto creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})  
    else:
        miFormularioproducto = AgregaProductoFormulario()
        return render(req, "agregaproducto.html", {"miFormularioproducto": miFormularioproducto})
    


def cliente(req,nombre):
    cliente = Cliente(nombre=nombre)
    cliente.save()
    return HttpResponse (f""" <p>Cliente: {cliente.nombre}<p>""")

#CRUD - READ
def lista_clientes(req):
    lista = Cliente.objects.all()
    return render(req, "cliente.html", {"lista_clientes":lista})

#CRUD - CREATE, PARA CREAR CLIENTES
def formulario(req: HttpRequest):
    print('method', req.method)
    print('post', req.POST)
    if req.method == 'POST':
        miFormulario = ClienteFormulario(req.POST)
        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data
            cliente = Cliente(nombre=data["nombre"], correo=data["correo"], direccion=data["direccion"])
            cliente.save()
            return render(req, "inicio.html", {"mensaje": "Cliente creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        miFormulario = ClienteFormulario()
        return render(req, "formulario.html", {"miFormulario": miFormulario})

#CRUD - DELETE, Elimina cliente

def eliminarcliente(req, id):

    if req.method == 'POST':

        cliente = Cliente.objects.get(id=id)
        cliente.delete()

        lista_clientes = Cliente.objects.all()

        return render(req, "cliente.html", {"lista_clientes": lista_clientes})
    
#CRUD - UPDATE, EDITAR CLIENTE
def editarcliente(req, id):

    cliente = Cliente.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = ClienteFormulario(req.POST)
        if miFormulario.is_valid():
            #print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            cliente.nombre = data["nombre"]
            cliente.correo = data["correo"]
            cliente.direccion = data["direccion"]
            cliente.save()
            return render(req, "inicio.html", {"mensaje": "Cliente creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        miFormulario = ClienteFormulario(initial={
            "nombre": cliente.nombre,
            "correo": cliente.correo,
            "direccion": cliente.direccion,
        })


        return render(req, "editarformulario.html", {"miFormulario": miFormulario, "id":cliente.id})



def busquedacliente(req):
    return render(req, "busqueda_cliente.html")

def buscarcliente(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        cliente = Cliente.objects.get (nombre=nombre)
        if cliente:
            return render(req,"resultadobuscar.html",{"cliente": cliente})   
    else:
        return HttpResponse ('No escribiste ningun cliente')


def pedido(req,nombre):
    pedido = Pedido(nombre=nombre)
    pedido.save()
    return HttpResponse (f""" <p>Pedido: {pedido.nombre}<p>""")

def lista_pedidos(req):
    lista = Pedido.objects.all()
    return render(req, "pedido.html", {"lista_pedidos":lista})


#VISTAS BASADAS EN CLASES

class ProductoList(ListView):
    model = Producto
    template_name = "producto_lista.html"
    context_object_name = "productos"

class ProductoDetail(DetailView):
    model = Producto
    template_name = "producto_detalle.html"
    context_object_name = "productos"

class ProductoCreate(LoginRequiredMixin,CreateView):
    model = Producto
    template_name = "producto_create.html"
    fields = ('__all__')
    success_url = '/app-shoperfumes/'

class ProductoUpdate(LoginRequiredMixin,UpdateView):
    model = Producto
    template_name = "producto_update.html"
    fields = ['nombre', 'precio', 'imagen']
    success_url = '/app-shoperfumes/'

class ProductoDelete(LoginRequiredMixin,DeleteView):
    model = Producto
    template_name =  "producto_delete.html"
    success_url = '/app-shoperfumes/'


#CLASES BASADA EN VISTAS, CLIENTES

class ClienteList(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = "cliente_lista.html"
    context_object_name = "clientes"

class ClienteDetail(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = "cliente_detalle.html"
    context_object_name = "clientes"

class ClienteCreate(LoginRequiredMixin,CreateView):
    model = Cliente
    success_url = '/app-shoperfumes/'
    fields = ['nombre']

class ClienteUpdate(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name = "cliente_update.html"
    success_url = '/app-shoperfumes/'
    fields = ['nombre', 'correo','direccion']

class ClienteDelete(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name =  "cliente_delete.html"
    success_url = '/app-shoperfumes/'


#VITA LOGIN USUARIO
def UsuarioLogin(req):

    if req.method == 'POST':
        form = AuthenticationForm(req, data = req.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contraseña)

            if user:
                login(req, user)
                        # Obtén el avatar del usuario
                try:
                    avatar = Avatar.objects.get(user=req.user.id)
                except:
                    avatar = None

                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}", "avatar": avatar})
            else:
                return render(req, "inicio.html", {"mensaje":"Datos incorrectos"})   
             
        else:
            return render(req, "inicio.html", {"mensaje":"Formulario Inválido"})
        
    else:
        form = AuthenticationForm()
        return render(req, "login.html", {"form": form})


# VISTA REGISTRO DE USUARIO
def UsuarioRegistro(req):

      if req.method == 'POST':

            #form = UserCreationForm(req.POST)
            form = UserRegisterForm(req.POST)
            if form.is_valid():

                  data= form.cleaned_data
                  usuario = data ["username"]
                 
                  form.save()
                  return render(req,"inicio.html" ,  {"mensaje":"Usuario Creado con Éxito!"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(req,"registro.html" ,  {"form":form})



#EDITAR PERFIL DEL USUARIO
def EditarPerfil(req):

    usuario = req.user

    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)
        
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Perfil actualizado con éxito"})
        else:
            return render(req, "inicio.html", {"miFomulario": miFormulario})
    else:

        miFormulario = UserEditForm(instance=req.user)

        return render(req, "editar_perfil.html", {"miFomulario": miFormulario})
    
#CREAR AVATAR  
def AgregarAvatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": f"Avatar actualizado con éxito!"})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregar_avatar.html", {"miFomulario": miFormulario})


def Acercademí(req):
    return render(req, "about.html")

def Escribenos(req):
    return render(req, "contacto.html")
