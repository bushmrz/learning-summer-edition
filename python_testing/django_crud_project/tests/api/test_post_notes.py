import uuid

import pytest
from rest_framework.test import APITestCase
from rest_framework import status

from note_api.models import NoteModel
from note_api.serializers import NoteSerializer


@pytest.mark.django_db
class NotePostAPITestCase(APITestCase):
    def test_post_note(self):
        url = "http://127.0.0.1:8000/api/notes/"
        data = {'title': 'Post Test Note',
                'content': 'This is a test note',
                'category': None}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        note = NoteModel.objects.get(title='Post Test Note')
        serializer = NoteSerializer(note)

        expected_data = {
            'data': {
                'note': serializer.data
            },
            'status': 'success'
        }

        self.assertEqual(response.data, expected_data)

    def test_filed_post_note(self):
        url = "http://127.0.0.1:8000/api/notes/"
        data = {'title': None,
                'content': 'This is a filed test note',
                'category': None}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        note = NoteModel.objects.get(content='This is a filed test note')
        serializer = NoteSerializer(note)

        expected_data = {
            'data': {
                'note': serializer.data
            },
            'status': 'success'
        }

        self.assertEqual(response.data, expected_data)

        