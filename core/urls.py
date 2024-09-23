from django.contrib import admin
from django.urls import path

from pages.views import homeView, aboutView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homeView),
    path('about/', aboutView),
]
