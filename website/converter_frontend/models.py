from django.db import models


# Create your models here.
class Currencies(models.Model):
    iso = models.CharField(
        max_length=3,
        unique=True,
        null=False,
    )
    num_code = models.CharField(
        max_length=3,
        unique=True,
        null=False,
    )
    symbol = models.CharField(
        max_length=5,
        blank=True,
        null=True,
    )
    currency_name = models.CharField(max_length=70)

    # Representation of this model in russian in admin backend
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class Rates(models.Model):
    date = models.DateField(
        default='1970-01-01',
        null=False,
        blank=False,
    )
    curr_id = models.ForeignKey(
        Currencies, on_delete=models.CASCADE
    )
    unit = models.IntegerField(
        default=1,
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        default=1,
    )
    unit = models.IntegerField(
        default=1,
    )

    # Representation of this model in russian in admin backend
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'