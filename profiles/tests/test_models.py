import pytest
from django.contrib.auth import get_user_model

from mixer.backend.django import mixer


User = get_user_model()
pytestmark = pytest.mark.django_db


class TestPost:
    def test_init(self):
        user = User.objects.create(email='Vasya@crab.com')
        obj = mixer.blend('profiles.Profile', user=user)
        assert obj.__str__() == 'Vasya@crab.com'
