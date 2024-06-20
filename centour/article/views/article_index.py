from django.views.generic import ListView

from article.models import Article


class IndexView(ListView):
    template_name = "article/index.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all()
