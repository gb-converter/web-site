from django.contrib import admin
from .models import Currencies, Rates


# Register your models here.
@admin.register(Currencies)
class CurrenciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso', 'num_code', 'symbol', 'currency_name',)
    list_filter = ('iso', )


@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display = ('date', 'curr_id', 'rate', )
    list_filter = ('date', 'curr_id', )
