from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from converter_frontend.models import Currencies, Rates
from .serializers import CurrenciesSerializer, RatesSerializer
import logging

logger = logging.getLogger(__name__)


class CurrenciesViewSet(viewsets.ModelViewSet):
    serializer_class = CurrenciesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Currencies.objects.all()


class RatesViewSet(viewsets.ModelViewSet):
    serializer_class = RatesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rates.objects.all()


def docs(request):
    logger.info('docs')
    return render(
        request,
        'api/docs.html',
        {
            'docs_components': {
                'Endpoints': f"{request.scheme}://{request.META['HTTP_HOST']}/api/v1/endpoints/",
                'Methods': f"{request.scheme}://{request.META['HTTP_HOST']}/api/v1/methods/",
            }
        }
    )


def methods(request):
    logger.info('methods')
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
    logger.info('endpoints')
    return render(
        request,
        'api/endpoints.html',
        {
            'endpoints': {
                'currencies': f"{request.scheme}://{request.META['HTTP_HOST']}/api/v1/currencies/",
                'currency': f"{request.scheme}://{request.META['HTTP_HOST']}/api/v1/currencies/<id>",
                'rates': f"{request.scheme}://{request.META['HTTP_HOST']}/api/v1/rates/"
            }
        }
    )
