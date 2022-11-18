from django.contrib import admin
from django.urls import path

from books.views import cadastroPatient, userTableAll

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userTableAll),
    path('cadastro', cadastroPatient, name='cadastro')
]
