import uuid
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_login_page_shows_login_form(client):
    """Login page shows login form for unauthenticated users."""

    response = client.get(reverse("login"))
    assert response.status_code == 200
    assert b"Login" in response.content
    assert b"username" in response.content
    assert b"password" in response.content


@pytest.mark.django_db
def test_authenticated_user_redirect_from_login_page(client, user):
    """Authenticated users trying to access login page are redirected to discover."""

    client.force_login(user)
    response = client.get(reverse("login"))
    assert response.status_code == 302
    assert response.url == reverse("discover")


@pytest.mark.django_db
def test_login_form_submission(client, user):
    """Test login form submission with valid credentials."""

    # Get the user model
    User = get_user_model()

    # Create a test user
    test_username = f"testuser_{uuid.uuid4()}"
    test_password = "testpassword"
    user = User.objects.create_user(username=test_username, password=test_password)

    # Submit login form with valid credentials
    response = client.post(reverse("login"), {
        "username": test_username,
        "password": test_password,
    })

    # Check for redirection to the discover page
    assert response.status_code == 302
    assert response.url == reverse("discover")

    # Verify that the user is authenticated
    user = User.objects.get(username=test_username)
    assert user is not None

    # Check if the user is logged in by verifying the session
    assert '_auth_user_id' in client.session

    # Optionally, login again and verify the response
    client.login(username=test_username, password=test_password)
    response = client.get(reverse("discover"))
    assert response.status_code == 200
