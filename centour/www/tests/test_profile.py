import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_profile_page(client, user):
    """Test the profile page for authenticated users."""

    client.force_login(user)
    response = client.get(reverse("profile"))
    assert response.status_code == 200
    assert b"Profile" in response.content
    assert b"Email:" in response.content
    assert user.email.encode() in response.content


@pytest.mark.django_db
def test_change_password_link(client, user):
    """Test the change password link on the profile page."""

    client.force_login(user)
    response = client.get(reverse("profile"))
    assert response.status_code == 200
    assert b"Change Password" in response.content

    change_password_response = client.get(reverse("change_password"))
    assert change_password_response.status_code == 200
    assert b"Change Password" in change_password_response.content
