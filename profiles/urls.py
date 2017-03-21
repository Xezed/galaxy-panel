from django.conf.urls import url

from profiles.views import ProfileView, RegistrationStep1View

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile'),
   url(r'^registration-step-1$', RegistrationStep1View.as_view(), name='reg_first_step'),
]