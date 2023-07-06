import pytest
from rest_framework.test import APIClient, APITestCase

from note_api.models import NoteModel

client = APIClient()


@pytest.mark.django_db
class NoteDetailAPITestCase(APITestCase):
    def setUp(self):
        self.note = NoteModel.objects.create(title="Test Note", content="This is a test note.")
        self.url = f"http://127.0.0.1:8000/api/notes/{self.note.id}"

    def test_get_notes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_note(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "success")
        self.assertEqual(response.data["data"]["note"]["title"], "Test Note")
        self.assertEqual(response.data["data"]["note"]["content"], "This is a test note.")

    def test_get_note_not_found(self):
        invalid_url = "http://127.0.0.1:8000/api/notes/9999/"
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["status"], "fail")
        self.assertEqual(response.data["message"], "Note with Id: 9999 not found")