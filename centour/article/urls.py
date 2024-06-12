from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("article/<uuid:pk>/", views.ArticleDetail.as_view(), name="article_detail"),
]
