from rest_framework import serializers

from converter_frontend.models import Currencies, Rates


# Serialisation - translating a data structure or object state
# into a format that can be stored

# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes
# that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization,
# allowing parsed data to be converted back into complex types, after first validating the incoming data.
class CurrenciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Currencies
        fields = ('id', 'iso', 'num_code', 'symbol', 'currency_name')


class RatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rates
        fields = ('date', 'curr_id', 'rate', 'unit')
