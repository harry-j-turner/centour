import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_redirects_to_login(client):
    """Index redirects to login for unauthenticated users."""

    response = client.get(reverse("index"))
    assert response.status_code == 302
    assert response.url == reverse("login")


@pytest.mark.django_db
def test_index_redirects_to_discover(client, user):
    """Index redirects to discover for authenticated users."""

    client.force_login(user)
    response = client.get(reverse("index"))
    assert response.status_code == 302
    assert response.url == reverse("discover")

