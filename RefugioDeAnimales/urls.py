"""RefugioDeAnimales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_confirm, password_reset_done, password_reset_complete
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascota/', include('apps.mascota.urls'),name="mascota"),
    path('adopcion/', include('apps.adopcion.urls'),name="adopcion"),
    path('usuario/', include('apps.usuario.urls'),name="usuario"),
    path('accounts/login/',login,kwargs={'template_name': 'index.html'}, name="login"),
    path('',login,kwargs={'template_name': 'index.html'}, name="login"),
    path('logout/',logout_then_login, name="logout"),

    #passwordResetPaths
    path('reset/passwordReset', password_reset, kwargs={'template_name':'passwordReset/passwordResetForm.html','email_template_name': 'passwordReset/passwordResetEmail.html'}, name='password_reset'), 

    path('reset/passwordResetDone', password_reset_done, kwargs={'template_name': 'passwordReset/passwordResetDone.html'}, name='password_reset_done'),

    path('reset/<uidb64>[0-9A-Za-z_\-]/<token>', password_reset_confirm, kwargs={'template_name': 'passwordReset/passwordResetConfirm.html'}, name='password_reset_confirm'),

    path('reset/done', password_reset_complete, kwargs={'template_name': 'passwordReset/passwordResetComplete.html'}, name='password_reset_complete'),
]
