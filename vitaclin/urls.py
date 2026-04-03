from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import connection

def criar_usuario(request):
    try:
        connection.ensure_connection()
    except:
        pass
    try:
        User.objects.create_superuser('vitaclin', '', 'vitaclin2026')
        return HttpResponse('Usuário criado!')
    except Exception as e:
        return HttpResponse(f'Erro: {e}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', lambda request: redirect('login'), name='home'),
    path('', include('pacientes.urls')),
    path('setup/', criar_usuario),
]