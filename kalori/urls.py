from django.urls import path

from . import views

app_name = 'kalori'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:food_id>/', views.detail, name='detail'),
]
