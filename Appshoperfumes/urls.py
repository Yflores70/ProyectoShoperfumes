from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import *
#AgregarAvatar,EditarPerfil, UsuarioRegistro, UsuarioLogin,ClienteDelete, ClienteUpdate,ClienteCreate,ClienteDetail,ClienteList,ProductoDelete, ProductoUpdate,ProductoCreate,ProductoDetail,ProductoList,agregacategoria,lista_categorias,inicio,lista_productos,agregarproducto,lista_clientes,formulario, busquedacliente,buscarcliente,eliminarcliente,editarcliente
urlpatterns = [
        path('', inicio, name='inicio'),
        #path('agrega-categoria/<nombre>', categoria),

        path('lista-blogs', BlogList.as_view(), name='lista-blogs'),
        path('detalle-blogs/<pk>', BlogDetail.as_view(), name='detalle-blogs'),
        path('crea-blogs', BlogCreate.as_view(), name='crea-blogs'),
         path('actualiza-blogs/<int:pk>/', BlogUpdate.as_view(), name='actualiza-blogs'),
        path('elimina-blogs/<pk>', BlogDelete.as_view(), name='elimina-blogs'),

        path('agregar-categorias', agregacategoria, name='agregar-categorias'),
        path('lista-categoria/', lista_categorias, name='categorias'),
        path('productos', lista_productos, name='productos'),
        path('agregar-productos', agregarproducto, name='agregar-productos'),

        path('clientes', lista_clientes, name='clientes'),
        path('agregar-clientes', formulario, name='agregar-clientes'),
        path('busqueda-clientes', busquedacliente, name='busqueda-clientes'),
        path('buscar-clientes/', buscarcliente, name='buscar-clientes'),
        path('eliminar-clientes/<int:id>', eliminarcliente, name='eliminar-clientes'),
        path('editar-clientes/<int:id>', editarcliente, name='editar-clientes'),

        path('lista-productos', ProductoList.as_view(), name='lista-productos'),
        path('detalle-productos/<pk>', ProductoDetail.as_view(), name='detalle-productos'),
        path('crea-productos', ProductoCreate.as_view(), name='crea-productos'),
        path('actualiza-productos/<pk>', ProductoUpdate.as_view(), name='actualiza-productos'),
        path('elimina-productos/<pk>', ProductoDelete.as_view(), name='elimina-productos'),

        path('lista-clientes', ClienteList.as_view(), name='lista-clientes'),
        path('detalle-clientes/<pk>', ClienteDetail.as_view(), name='detalle-clientes'),
        path('crea-clientes', ClienteCreate.as_view(), name='crea-clientes'),
        path('actualiza-clientes/<pk>', ClienteUpdate.as_view(), name='actualiza-clientes'),
        path('elimina-clientes/<pk>', ClienteDelete.as_view(), name='elimina-clientes'),
        
        path('login', UsuarioLogin, name='login'),
        path('registro', UsuarioRegistro, name='registro'),
        path('logout', LogoutView.as_view(template_name='inicio.html'), name='logout'), #se dirige a inicio

        path('edita-perfil', EditarPerfil, name='edita-perfil'),
        path('agregar-avatar', AgregarAvatar, name='agregar-avatar'),
        path('acerca-de-mí', Acercademí, name='acerca-de-mí'),
        path('contacto', Escribenos, name='contacto'),
        path('blog', Blog, name='blog'),
   

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)