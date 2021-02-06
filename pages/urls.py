from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.edit, name='edit'),
    path('<int:id>', views.delete, name='delete'),
]