"""webp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productos import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('empresa/',views.imformacion,name='informacion'),
    path('detalle/<int:idProducto>',views.detalles,name='detalle'),
    path('productos/',views.productos,name='productos'),
    path('categoria/<int:idCategoria>',views.filtroCategoria,name='filtroCategoria'),
    path('marca/<int:idMarca>',views.filtroMarca,name='filtroMarca'),
    path('contacto/',views.contacto,name='contacto'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
