from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    country = CountryField(default='RU')
    Personal_Entity = 'P'
    Legal_Entity = 'L'
    Entrepreneur_ = 'E'
    Government_Department = 'G'
    ENTITY_TYPES = (
        (Personal_Entity, _('Физическое лицо')),
        (Legal_Entity, _('Юридическое лицо')),
        (Entrepreneur_, _('Индивидуальный предпринематель')),
        (Government_Department, _('Государственное учреждение')),
    )
    entity_type = models.CharField(max_length=1, choices=ENTITY_TYPES, default=Personal_Entity)
    registered = models.BooleanField(default=False)

    # Content Type
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    # object_id = models.PositiveIntegerField(null=True)
    # content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.user


class PersonalEntity(models.Model):
    profile = models.OneToOneField(Profile)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=20)


class AbstractEntity(models.Model):
    profile = models.OneToOneField(Profile)
    name = models.CharField(max_length=120)
    incumbent = models.CharField(max_length=100)
    initials = models.CharField(max_length=120)
    foundation = models.CharField(max_length=120)
    inn = models.CharField(max_length=100)
    kpp = models.CharField(max_length=100)
    bik = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    kor_acc = models.CharField(max_length=100)
    acc = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    legal_addr = models.CharField(max_length=150)
    physic_addr = models.CharField(max_length=150)
    contact_entity = models.CharField(max_length=150)
    work_phone = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)

    class Meta:
        abstract = True


class LegalEntity(AbstractEntity):
    pass


class Entrepreneur(AbstractEntity):
    pass


class GovernmentDepartment(AbstractEntity):
    pass


