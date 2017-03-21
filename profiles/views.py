from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from profiles.forms import ProfileForm


class ProfileView(TemplateView):
    template_name = 'profiles/index.html'


class RegistrationStep1View(FormView):
    form_class = ProfileForm
    template_name = 'profiles/registration-step-1.html'
