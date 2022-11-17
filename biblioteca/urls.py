from django.contrib import admin
from django.urls import path

from books.views import userTableAll

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userTableAll),
    
]
