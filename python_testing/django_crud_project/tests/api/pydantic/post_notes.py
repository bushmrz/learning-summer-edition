from django.test import TestCase
from rest_framework.test import APIClient
from note_api.models import NotePostCreateModel


class PostCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_correct_note(self):
        request_data = {
            "title": "Test Post",
            "content": "This is a test post",
            "category": "Test"
        }
        post_data = NotePostCreateModel(**request_data)
        response = self.client.post('/api/notes/', data=post_data.dict())
        self.assertEqual(response.status_code, 201)

    def test_create_uncorrect_post(self):
        request_data = {
            "title": 1,
            "content": "This is a test post",
            "category": None
        }
        post_data = NotePostCreateModel(**request_data)
        response = self.client.post('/api/notes/', data=post_data.dict())
        self.assertEqual(response.status_code, 201)
