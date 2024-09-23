from django.contrib import admin
from django.urls import path

from pages.views import homeView, aboutView, cartView, contactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homeView),
    path('about/', aboutView),
    path('cart/', cartView),
    path('contact/', contactView)
]
