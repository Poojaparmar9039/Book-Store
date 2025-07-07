from django.urls import path
from . import views


urlpatterns = [
    path('', views.Books, name="Books"),
    path('AddToCart/<int:id>/', views.AddToCart, name="AddToCart"),
    path('DeleteFromCart/<int:id>/',views.DeleteFromCart, name="DeleteFromCart"),
    path('BookDetails/<int:id>/', views.BookDetails, name="BookDetails"),
    path('ReadBook/<int:id>/', views.ReadBook, name="ReadBook"),
    path('SendToAi', views.SendToAi, name="SendToAi"),
  
]

