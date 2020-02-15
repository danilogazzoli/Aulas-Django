from django.urls import path
from .views import index, setacookie, redireciona
from . import views


app_name = "aula3"

urlpatterns = [
    path('', index),
    path('cookie', setacookie),
    path('uol', redireciona),
    path('<int:code>', views.show_code),
    path('cats/<int:code>',views.go_cats),
    path('get/', views.show_get_values),
    path('post/', views.show_post_values)
]
