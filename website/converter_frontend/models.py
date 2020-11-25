from django.db import models


# Create your models here.
class Currencies(models.Model):
    id = models.IntegerField(
        primary_key=True,
    )
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
    unit = models.IntegerField(
        default=1,
    )
    currency_name = models.CharField(max_length=70)


class Rates(models.Model):
    date = models.DateField(
        default='1970-01-01',
        null=False,
        blank=False,
    )
    curr_id = models.ForeignKey(
        Currencies, on_delete=models.CASCADE
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        default=1,
    )
