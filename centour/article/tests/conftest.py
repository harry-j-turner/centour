import pytest
from django.test import Client

from article.models import Article


@pytest.fixture
def create_user(django_user_model):
    return django_user_model.objects.create_user(username="testuser", password="123456")


@pytest.fixture(scope="session")
def authenticated_client():
    def _authenticated_client(test_user):
        client = Client()
        client.force_login(test_user)

        return client

    return _authenticated_client


@pytest.fixture(scope="session")
def create_article():
    def _create_article(owner, **kwargs):
        return Article.objects.create(
            owner=owner,
            title=kwargs.get("title", "Test article"),
            content=kwargs.get("content", "Test content"),
        )

    return _create_article
