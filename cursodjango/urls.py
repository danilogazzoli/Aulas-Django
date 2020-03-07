"""cursodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from aula3.views import index
from aula4.views import index
from aula6.views import index as index6
from aula7.views import index as index7, restrita, logout_view, permission_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("aula3.urls")),
    path('aula4', index),
    path('aula6', index6),
    path('entrar', index7, name='login'),
    path('aula7/restrita', restrita),
    path('aula7/sair', logout_view),
    path('aula7/view-carrinho', permission_view)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
