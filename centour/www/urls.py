from django.urls import path

from .views import IndexView, DiscoverView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("discover/", DiscoverView.as_view(), name="discover"),
]
