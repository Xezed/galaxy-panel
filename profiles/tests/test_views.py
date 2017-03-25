import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls.base import reverse

from mixer.backend.django import mixer

from profiles.models import Profile

User = get_user_model()
pytestmark = pytest.mark.django_db


class TestProfileView:
    def test_authenticate(self, client):
        response = client.get(reverse('profile'))
        assert response.status_code == 302
        assert 'login' in response.url


class TestRegistrationView(TestCase):
    def test_registration_first_step(self):
        client = Client()
        path = reverse('reg_first_step')
        response = client.get(path)
        assert response.status_code == 302
        assert 'login' in response.url
        user = User.objects.create(email='q@q.ru', password='test')
        user2 = User.objects.create(email='qq@q.ru', password='test')
        user3 = User.objects.create(email='qqq@q.ru', password='test')
        user4 = User.objects.create(email='qqqq@q.ru', password='test')
        client.force_login(user)
        response = client.get(path)
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'profiles/registration-step-1.html')
        assert Profile.objects.count() == 0

        data_pers = {
            'country': 'RU',
            'entity_type': 'P'
        }
        data_legal = {
            'country': 'RU',
            'entity_type': 'L'
        }
        data_entrpr = {
            'country': 'RU',
            'entity_type': 'E'
        }
        data_gov = {
            'country': 'RU',
            'entity_type': 'G'
        }

        response = client.post(path=path, data=data_pers)
        assert response.status_code == 302
        assert Profile.objects.count() == 1
        assert Profile.objects.first().registered is False
        response = client.get(path)
        self.assertTemplateUsed(response, 'profiles/registration-step-2-person.html')
        response = client.get(reverse('reg_cancel'), follow=True)
        assert Profile.objects.count() == 0
        self.assertTemplateUsed(response, 'profiles/registration-step-1.html')
        response = client.get(reverse('reg_cancel'), follow=True)
        self.assertTemplateUsed(response, 'profiles/registration-step-1.html')
        response = client.post(path=path, data=data_pers)

        client2 = Client()
        client3 = Client()
        client4 = Client()
        client2.force_login(user2)
        client3.force_login(user3)
        client4.force_login(user4)

        response = client2.post(path=path, data=data_legal)
        assert response.status_code == 302
        assert Profile.objects.count() == 2
        response = client2.get(path)
        self.assertTemplateUsed(response, 'profiles/registration-step-2-legal.html')

        response = client3.post(path=path, data=data_entrpr)
        assert response.status_code == 302
        assert Profile.objects.count() == 3
        response = client3.get(path)
        self.assertTemplateUsed(response, 'profiles/registration-step-2-enterpr.html')

        response = client4.post(path=path, data=data_gov)
        assert response.status_code == 302
        assert Profile.objects.count() == 4
        response = client4.get(path)
        self.assertTemplateUsed(response, 'profiles/registration-step-2-gov.html')

        data_2 = {
            'name': 'asdf',
            'incumbent': 'asdf',
            'foundation': 'asdf',
            'initials': 'fasd',
            'inn': 'asdf',
            'kpp': 'aasdf',
            'bik': 'asdf',
            'bank': 'asdf',
            'kor_acc': 'asdf',
            'acc': 'fasdf',
            'address': 'asdf',
            'legal_addr': 'asdf',
            'physic_addr': 'asdfasd',
            'contact_entity': 'asdfsad',
            'work_phone': 'asdf',
            'phone': 'asdf'
        }

        data_2_pers = {
            'first_name': 'asdf',
            'last_name': 'asdf',
            'sur_name': 'asdf',
            'phone_number': '123456',
        }

        response = client.post(path=path, data=data_2_pers, follow=True)
        response_1 = client2.post(path=path, data=data_2, follow=True)
        response_2 = client3.post(path=path, data=data_2, follow=True)
        response_3 = client4.post(path=path, data=data_2, follow=True)

        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertTemplateUsed(response_1, 'profiles/index.html')
        self.assertTemplateUsed(response_2, 'profiles/index.html')
        self.assertTemplateUsed(response_3, 'profiles/index.html')

        response = client.post(path=path, data=data_2_pers, follow=True)
        self.assertTemplateUsed(response, 'profiles/index.html')

        response = client.get(reverse('reg_cancel'), follow=True)
        self.assertTemplateUsed(response, 'profiles/index.html')
