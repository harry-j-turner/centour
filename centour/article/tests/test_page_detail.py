import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_article_detail_returns_single_article(authenticated_client, create_user, create_article, django_user_model):
    user = create_user

    article = create_article(owner=user, title="Article 1", content="Content 1")

    url = reverse("article_detail", kwargs={"pk": article.pk})
    response = authenticated_client(user).get(url)
    data = response.context["article"]

    assert response.status_code == 200
    assert data.title == "Article 1"
    assert data.content == "Content 1"
