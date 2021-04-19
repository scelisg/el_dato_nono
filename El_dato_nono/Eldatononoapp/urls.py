

from django.urls import path
from Eldatononoapp import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('registro/',views.registro,name="Registro"),
    path('login/',views.login, name="Login"),
]