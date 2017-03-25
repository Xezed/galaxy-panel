from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView

from profiles.forms import ProfileForm, PersonalEntityForm, LegalEntityForm, EntrepreneurForm, GovernmentDepartmentForm
from profiles.models import Profile


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/index.html'


class RegistrationStep1View(LoginRequiredMixin, FormView):
    form_class = ProfileForm
    template_name = 'profiles/registration-step-1.html'
    success_url = reverse_lazy('reg_first_step')

    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return super(RegistrationStep1View, self).get(request, *args, **kwargs)

        if profile.registered is False:
            if profile.entity_type is 'P':
                form = PersonalEntityForm()
                template = 'profiles/registration-step-2-person.html'
                context = {'form': form}
                return render(self.request, template, context)
            if profile.entity_type is 'L':
                form = LegalEntityForm()
                template = 'profiles/registration-step-2-legal.html'
                context = {'form': form}
                return render(self.request, template, context)
            if profile.entity_type is 'E':
                form = EntrepreneurForm()
                template = 'profiles/registration-step-2-enterpr.html'
                context = {'form': form}
                return render(self.request, template, context)
            if profile.entity_type is 'G':
                form = GovernmentDepartmentForm()
                template = 'profiles/registration-step-2-gov.html'
                context = {'form': form}
                return render(self.request, template, context)
        else:
            return redirect('profile')

    def post(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            form = self.get_form()
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return HttpResponseRedirect(self.success_url)

        if profile.registered is False:
            if profile.entity_type is 'P':
                form = self.get_form(form_class=PersonalEntityForm)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.profile = profile
                    profile.registered = True
                    instance.save()
                    profile.save()

                    return HttpResponseRedirect(self.success_url)

            if profile.entity_type is 'L':
                form = self.get_form(form_class=LegalEntityForm)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.profile = profile
                    profile.registered = True
                    instance.save()
                    profile.save()

                    return HttpResponseRedirect(self.success_url)

            if profile.entity_type is 'E':
                form = self.get_form(form_class=EntrepreneurForm)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.profile = profile
                    profile.registered = True
                    instance.save()
                    profile.save()

                    return HttpResponseRedirect(self.success_url)

            if profile.entity_type is 'G':
                form = self.get_form(form_class=GovernmentDepartmentForm)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.profile = profile
                    profile.registered = True
                    instance.save()
                    profile.save()

                    return HttpResponseRedirect(self.success_url)
        else:
            return redirect('profile')


class CancelRegistration(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return redirect('reg_first_step')

        if profile.registered:
            return redirect('reg_first_step')
        else:
            profile.delete()
            return redirect('reg_first_step')
