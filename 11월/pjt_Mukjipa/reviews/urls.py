from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("store/", views.store, name="store"),
    path("<int:store_pk>/", views.store_detail, name="store_detail"),
    path("<int:store_pk>/delete", views.store_delete, name="store_delete"),
    path("<int:store_pk>/update", views.store_update, name="store_update"),
    path("<int:store_pk>/review_create/", views.review_create, name="review_create"),
    path(
        "<int:store_pk>/<int:review_pk>/review_detail/",
        views.review_detail,
        name="review_detail",
    ),
    path(
        "<int:store_pk>/<int:review_pk>/review_delete/",
        views.review_delete,
        name="review_delete",
    ),
    path(
        "<int:store_pk>/<int:review_pk>/review_detail/review_update/",
        views.review_update,
        name="review_update",
    ),
    path("search/", views.search, name="search"),
    path(
        "<int:store_pk>/<int:review_pk>/review_detail/comment/",
        views.comment_create,
        name="comment_create",
    ),
    path(
        "<int:store_pk>/<int:review_pk>/review_detail/comment/<int:comment_pk>/comment_delete",
        views.comment_delete,
        name="comment_delete",
    ),
    path("local_list/", views.local_list, name="local_list"),
    path("local_list/local_detail_gn", views.local_detail_gn, name="local_detail_gn"),
    path("local_list/local_detail_sc", views.local_detail_sc, name="local_detail_sc"),
    path("local_list/local_detail_ys", views.local_detail_ys, name="local_detail_ys"),
    path("local_list/local_detail_sd", views.local_detail_sd, name="local_detail_sd"),
    path("local_list/local_detail_no", views.local_detail_no, name="local_detail_no"),
    path("local_list/local_detail_dj", views.local_detail_dj, name="local_detail_dj"),
    path("local_list/local_detail_sp", views.local_detail_sp, name="local_detail_sp"),
    path("local_list/local_detail_jn", views.local_detail_jn, name="local_detail_jn"),
    path("price_list/", views.price_list, name="price_list"),
    path(
        "price_list/price_detail_1man",
        views.price_detail_1man,
        name="price_detail_1man",
    ),
    path(
        "price_list/price_detail_2man",
        views.price_detail_2man,
        name="price_detail_2man",
    ),
    path(
        "price_list/price_detail_3man",
        views.price_detail_3man,
        name="price_detail_3man",
    ),
    path(
        "price_list/price_detail_4man",
        views.price_detail_4man,
        name="price_detail_4man",
    ),
    path(
        "price_list/price_detail_4manup",
        views.price_detail_4manup,
        name="price_detail_4manup",
    ),
]
