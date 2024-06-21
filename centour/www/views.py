from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from entry.models import Entry


class IndexView(View):
    def get(self, request):

        if request.user.is_authenticated:
            return redirect("discover")

        return redirect("login")


class LoginView(auth_views.LoginView):
    def get(self, request):

        if request.user.is_authenticated:
            return redirect("discover")

        return super().get(request)


class DiscoverView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("index")

        entries = Entry.objects.all()
        return render(request, "www/discover.html", {"entries": entries})


class EntryDetailView(View):
    def get(self, request, uuid):
        entry = get_object_or_404(Entry, uuid=uuid)
        return render(request, "www/entry.html", {"entry": entry})
