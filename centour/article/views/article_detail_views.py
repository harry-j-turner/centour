from django.views.generic import DetailView

from article.models import Article


class ArticleDetail(DetailView):
    template_name = "article/article_detail/article_detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.all()
