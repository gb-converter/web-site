from rest_framework import serializers

from website.converter_frontend.models import Currencies, Rates


class CurrenciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Currencies
        fields = ('id', 'iso', 'num_code', 'symbol', 'unit', 'currency_name')


class RatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rates
        fields = ('date', 'curr_id', 'rate')
