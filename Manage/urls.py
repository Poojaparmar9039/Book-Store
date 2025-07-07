from django.urls import path
from . import views


urlpatterns = [
    path('',views.manage,name='manage'),
    path('Addbook/',views.Addbook, name='Addbook'),
]
