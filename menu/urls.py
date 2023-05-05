from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menupage, name='best_menu'),
]