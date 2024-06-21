from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):
    def get(self, request):

        if request.user.is_authenticated:
            return redirect("discover")

        return render(request, "www/index.html")


class DiscoverView(View):
    def get(self, request):
        return render(request, "www/discover.html")
