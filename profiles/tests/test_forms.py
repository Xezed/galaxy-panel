import pytest

from profiles.forms import PersonalEntityForm

pytestmark = pytest.mark.django_db


class TestPersonalEntityForm:
    def test_init(self):
        form_data = {'first_name': 'alex',
                     'last_name': '',
                     'sur_name': '',
                     'phone_number': '123'}
        form = PersonalEntityForm(data=form_data)

        assert form.is_valid() is False

        form_data['last_name'] = 'bosh'
        form = PersonalEntityForm(data=form_data)

        assert form.is_valid() is True
