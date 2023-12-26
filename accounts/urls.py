from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from accounts.views import login_request, pagina_perfil, registro_usuario, editar_request, editar_avatar_request, \
        logout_view

urlpatterns = [
        path('registro/', registro_usuario, name='registro_usuario'),
        path('login/', login_request, name='login'),
        path('perfil/', pagina_perfil, name= 'perfil'),
        path('editar/', editar_request, name="Editar"),
        path('avatar/', editar_avatar_request, name="Avatar"),
        path('logout/', logout_view, name='logout')

]