from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy

from entry.models import Entry
from entry.forms import EntryForm


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


class ChangePasswordFormView(auth_views.PasswordChangeView):
    template_name = "registration/change_password_form.html"
    success_url = reverse_lazy("password_change_done")


class ChangePasswordDoneView(auth_views.PasswordChangeDoneView):
    template_name = "registration/change_password_done.html"


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("index")

        return render(request, "www/profile.html")

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


class EntryFormView(View):
    def get(self, request, uuid=None):
        if not request.user.is_authenticated:
            return redirect("index")

        if uuid:
            entry = get_object_or_404(Entry, uuid=uuid)
            form = EntryForm(instance=entry)
        else:
            form = EntryForm()

        return render(request, "www/entry_form.html", {"form": form, "uuid": uuid})

    def post(self, request, uuid=None):
        if not request.user.is_authenticated:
            return redirect("index")

        if uuid:
            entry = get_object_or_404(Entry, uuid=uuid)
            form = EntryForm(request.POST, instance=entry)
        else:
            form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("discover")

        return render(request, "www/entry_form.html", {"form": form, "uuid": uuid})
