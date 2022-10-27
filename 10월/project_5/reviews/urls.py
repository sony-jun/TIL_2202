from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path('', views.reviews_article, name="reviews-article"),
    path('create/', views.reviews_create, name="reviews-create"),
    path('detail/<int:pk>/', views.reviews_detail, name="reviews-detail"),
    path('update/<int:pk>/', views.reviews_update, name="reviews-update"),
    path('delete/<int:pk>/', views.reviews_delete, name="reviews-delete"),    
]