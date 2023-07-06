import pytest
from rest_framework.test import APITestCase
from rest_framework import status

from note_api.models import NoteModel

@pytest.mark.django_db
class NotePatchAPITestCase(APITestCase):
    def setUp(self):
        self.note = NoteModel.objects.create(title="Test Note", content="This is a test note.")
        self.url = f"http://127.0.0.1:8000/api/notes/{self.note.id}"

    def test_patch_note(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        response = self.client.patch(self.url, content='New text', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


