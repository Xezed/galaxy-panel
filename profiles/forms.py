from django import forms
from django.utils.safestring import mark_safe
from django_countries.widgets import CountrySelectWidget

from profiles.models import Profile, PersonalEntity, LegalEntity, Entrepreneur, GovernmentDepartment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['entity_type', 'country']
        widgets = {'country': CountrySelectWidget(
            attrs={'class': 'form-control select2 select2-hidden-accessible',
                   'style': 'width: 96%;',
                   'tabindex': '-1', 'aria-hidden': 'true'},
            layout='{widget}<img class="country-select-flag" id="{flag_id}" style="margin: 6px 4px" src="{country.flag}">'
        ), 'entity_type': forms.RadioSelect(
            attrs={'class': 'flat-red', 'style': 'position: absolute; opacity: 0;'}
        )}


class PersonalEntityForm(forms.ModelForm):
    class Meta:
        model = PersonalEntity
        fields = ['first_name', 'last_name', 'sur_name', 'phone_number']
        labels = {
            'first_name': ('Имя'),
            'last_name': ('Фамилия'),
            'sur_name': ('Отчество (необязательно)'),
            'phone_number': mark_safe('Телефон <br/> Вам будет отправлено смс с кодом.  Зарегистрировать новый аккаунт с данным номером будет невозможно.'),
        }


class EntityForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'incumbent', 'initials', 'foundation', 'inn', 'kpp', 'bik', 'bank', 'kor_acc',
                  'acc', 'address', 'legal_addr', 'physic_addr', 'contact_entity', 'work_phone', 'phone']
        # labels = {
        #     'name',
        #     'incumbent',
        #     'initials',
        #     'inn',
        #     'kpp',
        #     'bik',
        #     'bank',
        #     'kor_acc',
        #     'acc',
        #     'address',
        #     'legal_addr',
        #     'physic_addr',
        #     'contact_entity',
        #     'work_phone',
        #     'phone'
        # }


class LegalEntityForm(EntityForm):
    class Meta(EntityForm.Meta):
        model = LegalEntity


class EntrepreneurForm(EntityForm):
    class Meta(EntityForm.Meta):
        model = Entrepreneur


class GovernmentDepartmentForm(EntityForm):
    class Meta(EntityForm.Meta):
        model = GovernmentDepartment
