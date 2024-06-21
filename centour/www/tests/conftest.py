import pytest


@pytest.fixture(scope="function")
def user(django_user_model):
    return django_user_model.objects.create_user(username="testuser", password="123456")
