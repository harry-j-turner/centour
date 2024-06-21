from django.urls import path

from .views import IndexView, DiscoverView, LoginView, EntryDetailView, EntryFormView, ProfileView, ChangePasswordDoneView, ChangePasswordFormView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("discover/", DiscoverView.as_view(), name="discover"),
    path("login/", LoginView.as_view(), name="login"),
    path('entry/<uuid:uuid>/', EntryDetailView.as_view(), name='entry_detail'),
    path('entry/form/', EntryFormView.as_view(), name='entry_form'),
    path('entry/form/<uuid:uuid>/', EntryFormView.as_view(), name='entry_form'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('accounts/change_password/', ChangePasswordFormView.as_view(), name='change_password'),
    path('accounts/change_password_done/', ChangePasswordDoneView.as_view(), name='password_change_done'),
]
