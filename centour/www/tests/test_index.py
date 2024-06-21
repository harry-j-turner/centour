import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_shows_login(client):
    """Index shows login button for unauthenticated users."""

    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert b"Login" in response.content


@pytest.mark.django_db
def test_index_redirects_to_discover(client, user):
    """Index redirects to discover for authenticated users."""

    client.force_login(user)
    response = client.get(reverse("index"))
    assert response.status_code == 302
    assert response.url == reverse("discover")
