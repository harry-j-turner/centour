import pytest
from django.urls import reverse
from entry.models import Entry


@pytest.mark.django_db
def test_entry_detail_page(client, user):
    """Entry detail page shows title and content of the entry."""

    entry = Entry.objects.create(title="Test Entry", content="Detailed content for the entry", is_public=True)

    client.force_login(user)
    response = client.get(reverse("entry_detail", kwargs={"uuid": entry.uuid}))
    assert response.status_code == 200
    assert b"Test Entry" in response.content
    assert b"Detailed content for the entry" in response.content


@pytest.mark.django_db
def test_create_entry(client, user):
    """Test authenticated user can create a new entry."""

    client.force_login(user)
    response = client.get(reverse("entry_form"))
    assert response.status_code == 200

    create_response = client.post(reverse("entry_form"), {
        "title": "New Entry",
        "content": "Content for new entry",
        "is_public": True,
    })

    assert create_response.status_code == 302  # Redirects after successful creation
    assert Entry.objects.filter(title="New Entry").exists()


@pytest.mark.django_db
def test_edit_entry(client, user):
    """Test the page for editing an existing entry."""

    entry = Entry.objects.create(title="Old Title", content="Old content", is_public=True)

    client.force_login(user)
    response = client.get(reverse("entry_form", kwargs={"uuid": entry.uuid}))
    assert response.status_code == 200

    edit_response = client.post(reverse("entry_form", kwargs={"uuid": entry.uuid}), {
        "title": "Updated Title",
        "content": "Updated content",
        "is_public": True,
    })

    assert edit_response.status_code == 302  # Redirects after successful update
    entry.refresh_from_db()
    assert entry.title == "Updated Title"
    assert entry.content == "Updated content"
