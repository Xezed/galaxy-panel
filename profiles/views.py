from django.shortcuts import render
from django.views.generic.edit import FormView

from profiles.forms import ProfileForm


class ProfileView(FormView):
    form_class = ProfileForm
    template_name = 'profile.html'
