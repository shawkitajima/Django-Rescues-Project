from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rescues/', views.rescues_index, name = 'index'),
    path('rescues/<int:rescue_id>/', views.rescues_detail, name = 'detail'),
]