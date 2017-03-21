from django import forms
from django_countries.widgets import CountrySelectWidget

from profiles.models import Profile


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

