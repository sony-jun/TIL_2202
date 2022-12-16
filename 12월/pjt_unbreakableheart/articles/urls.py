from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("calendar", views.calendar, name="calendar"),
    path("", views.articles_index, name="articles_index"),
    path("articles_create/", views.articles_create, name="articles_create"),
    path("song_search/", views.song_search, name="song_search"),
    path(
        "<int:articles_pk>/articles_detail/",
        views.articles_detail,
        name="articles_detail",
    ),
    path(
        "<int:articles_pk>/articles_delete/",
        views.articles_delete,
        name="articles_delete",
    ),
    path(
        "<int:articles_pk>/articles_update/",
        views.articles_update,
        name="articles_update",
    ),
    path(
        "<int:articles_pk>/articles_detail/comments/",
        views.comment_create,
        name="comment_create",
    ),
    path(
        "<int:articles_pk>/articles_detail/comments/<int:comment_pk>/comment_delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path(
        "<int:articles_pk>/articles_declaration/",
        views.articles_declaration,
        name="articles_declaration",
    ),
    path(
        "<int:articles_pk>/<int:comment_pk>/comment_declaration",
        views.comment_declaration,
        name="comment_declaration",
    ),
    path("id-sort/", views.id_sort, name="id_sort"),
    path("calendar-detail/<str:date>/", views.calendar_detail, name="calendar_detail"),
    path('<int:articles_pk>/happy/', views.happy, name="happy"),
    path('<int:articles_pk>/sad/', views.sad, name="sad"),
    path('<int:articles_pk>/angry/', views.angry, name="angry"),
    path('<int:articles_pk>/funny/', views.funny, name="funny"),
]
