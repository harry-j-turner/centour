import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from article.models import Article


class ArticleDetail(LoginRequiredMixin, DetailView):
    template_name = "article/article_detail/article_detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.all()
