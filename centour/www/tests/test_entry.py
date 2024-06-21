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
