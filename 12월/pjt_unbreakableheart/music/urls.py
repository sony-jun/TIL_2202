from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path("search/", views.search, name="search"),
    path('create/', views.create, name='create'),
]
