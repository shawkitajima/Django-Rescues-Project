from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rescues/', views.rescues_index, name = 'index'),
    path('rescues/<int:rescue_id>/', views.rescues_detail, name = 'detail'),
    path('rescues/create', views.RescueCreate.as_view(), name = 'rescue_create'),
    path('rescues/<int:pk>/update/', views.RescueUpdate.as_view(), name = 'rescue_update'),
    path('rescues/<int:pk>/delete/', views.RescueDelete.as_view(), name = 'rescue_delete'),
    path('rescues/<int:rescue_id>/add_gift/', views.add_gift, name = 'add_gift'),
    path('rescues/<int:rescue_id>/assoc_adopter/<int:adopter_id>/', views.assoc_adopter, name = 'assoc_adopter'),
    path('rescues/<int:rescue_id>/disassoc_adopter/<int:adopter_id>/', views.disassoc_adopter, name = 'disassoc_adopter'),
    path('adopters/', views.AdopterList.as_view(), name = 'adopters_index'),
    path('adopters/<int:pk>/', views.AdopterDetail.as_view(), name = 'adopters_detail'),
    path('adopters/create/', views.AdopterCreate.as_view(), name = 'adopters_create'),
    path('adopters/<int:pk>/update/', views.AdopterUpdate.as_view(), name = 'adopters_update'),
    path('adopters/<int:pk>/delete/', views.AdopterDelete.as_view(), name = 'adopters_delete'),
    ]