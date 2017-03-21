from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    country = CountryField(default='RU')
    Personal_Entity = 'P'
    Legal_Entity = 'L'
    Entrepreneur_ = 'E'
    Government_Department = 'G'
    ENTITY_TYPES = (
        (Personal_Entity, 'Физическое лицо'),
        (Legal_Entity, 'Юридическое лицо'),
        (Entrepreneur_, 'Индивидуальный предпринематель'),
        (Government_Department, 'Государственное учреждение'),
    )
    entity_type = models.CharField(max_length=1, choices=ENTITY_TYPES, default=Personal_Entity)

    # Content Type
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.user


class PersonalEntity(models.Model):
    email = models.EmailField()
    profile = GenericRelation(Profile)


class LegalEntity(models.Model):
    phone_number = models.PositiveIntegerField()
    profile = GenericRelation(Profile)


class Entrepreneur(models.Model):
    firm_name = models.CharField(max_length=120)
    profile = GenericRelation(Profile)


class GovernmentDepartment(models.Model):
    profile = GenericRelation(Profile)


