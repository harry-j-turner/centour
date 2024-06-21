import pytest
from django.urls import reverse

from entry.models import Entry


@pytest.mark.django_db
def test_discover_redirects_to_index(client):
    """Discover redirects to index for unauthenticated users."""

    response = client.get(reverse("discover"))
    assert response.status_code == 302
    assert response.url == reverse("index")


@pytest.mark.django_db
def test_discover_shows_logout_button(client, user):
    """Discover shows logout button for authenticated users."""

    client.force_login(user)
    response = client.get(reverse("discover"))
    assert response.status_code == 200
    assert b"Logout" in response.content


@pytest.mark.django_db
def test_discover_shows_profile_button(client, user):
    """Discover shows profile button for authenticated users."""

    client.force_login(user)
    response = client.get(reverse("discover"))
    assert response.status_code == 200
    assert b"Profile" in response.content


@pytest.mark.django_db
def test_username_shown(client, user):
    """Discover shows the username of the authenticated user."""

    client.force_login(user)
    response = client.get(reverse("discover"))
    assert response.status_code == 200
    assert user.username.encode() in response.content


@pytest.mark.django_db
def test_discover_shows_a_create_entry_button(client, user):
    """Discover shows a button to create a new entry for authenticated users."""

    client.force_login(user)
    response = client.get(reverse("discover"))
    assert response.status_code == 200
    assert b"Create new entry" in response.content


@pytest.mark.django_db
def test_discover_shows_entries(client, user):
    """Discover page shows entries for authenticated users."""

    # Create test entries
    Entry.objects.create(title="Test Entry 1", content="Content for entry 1", is_public=True)
    Entry.objects.create(title="Test Entry 2", content="Content for entry 2", is_public=True)

    client.force_login(user)
    response = client.get(reverse("discover"))
    assert response.status_code == 200
    assert b"Test Entry 1" in response.content
    assert b"Test Entry 2" in response.content
