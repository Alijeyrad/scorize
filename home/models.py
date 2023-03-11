from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class University(models.Model):
    class Meta:
        verbose_name_plural = _('universities')

    PUBLIC = 'public university'
    PRIVATE = 'private university'
    ARTS = 'liberal arts college'
    COMMUNITY = 'community college'

    TYPE_CHOICES = [
        (PUBLIC, PUBLIC),
        (PRIVATE, PRIVATE),
        (ARTS, ARTS),
        (COMMUNITY, COMMUNITY),
    ]
    
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=15)
    logo_pic = models.ImageField(upload_to="logos")
    overview =  models.TextField()
    date_established = models.DateField()
    total_students = models.PositiveIntegerField()
    international_students = models.PositiveIntegerField()
    website = models.URLField()
    acceptance_rate = models.FloatField()

    uni_type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
    )

    def __str__(self) -> str:
        return f'{self.name}'

class City(models.Model):
    class Meta:
        verbose_name_plural = _('cities')

    name = models.CharField('city name', max_length=100,)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'


class Country(models.Model):
    class Meta:
        verbose_name_plural = _('countries')

    name = models.CharField('country name', max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'
