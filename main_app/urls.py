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
]