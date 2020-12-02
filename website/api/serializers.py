from rest_framework import serializers

from converter_frontend.models import Currencies, Rates


# Serialisation - translating a data structure or object state
# into a format that can be stored
class CurrenciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Currencies
        fields = ('id', 'iso', 'num_code', 'symbol', 'currency_name')


class RatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rates
        fields = ('date', 'curr_id', 'rate', 'unit')
