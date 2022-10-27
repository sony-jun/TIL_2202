from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/follow/", views.follow, name="follow"),
    path("update/", views.update, name="update"),
]
