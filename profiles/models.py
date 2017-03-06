from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    limit = models.Q(app_label='profiles', model='personalentity') \
          | models.Q(app_label='profiles', model='legalentity') \
          | models.Q(app_label='profiles', model='entrepreneur')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.user


class PersonalEntity(models.Model):
    email = models.EmailField()


class LegalEntity(models.Model):
    phone_number = models.PositiveIntegerField()


class Entrepreneur(models.Model):
    firm_name = models.CharField(max_length=120)


