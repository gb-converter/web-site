from django.shortcuts import render
from rest_framework import viewsets
from converter_frontend.models import Currencies, Rates
from .serializers import CurrenciesSerializer, RatesSerializer


class CurrenciesViewSet(viewsets.ModelViewSet):
    serializer_class = CurrenciesSerializer

    def get_queryset(self):
        return Currencies.objects.all()


class RatesViewSet(viewsets.ModelViewSet):
    serializer_class = RatesSerializer

    def get_queryset(self):
        return Rates.objects.all()


def docs(request):
    return render(
        request,
        'api/docs.html',
        {
            'docs_components': {
                'Endpoints': 'https://github.com/gb-converter?tab=projects',
                'Methods': 'https://github.com/gb-converter/api'
            }
        }
    )


def methods(request):
    return render(
        request,
        'api/methods.html',
        {
            'methods': {
                'POST': 'Create',
                'GET': 'Read',
                'PUT': 'Update',
                'DELETE': 'Delete'
            }
        }
    )


def endpoints(request):
    return render(
        request,
        'api/endpoints.html',
        {
            'endpoints': {
                'currency': 'url to manipulate currencies via api',
                'rates': 'url to manipulate currency rates via api'
            }
        }
    )
