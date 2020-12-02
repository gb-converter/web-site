from django.urls import path
from rest_framework import routers
from .views import (
    CurrenciesViewSet,
    RatesViewSet,
    docs,
    methods,
    endpoints
)

# Explanation
# https://www.django-rest-framework.org/api-guide/routers/
# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter

# REST framework adds support for automatic URL routing to Django,
# and provides you with a simple, quick and consistent way of
# wiring your view logic to a set of URLs.

router = routers.DefaultRouter()

router.register('currencies', CurrenciesViewSet, basename='currencies')
router.register('rates', RatesViewSet, basename='rates')

# url dispatcher namespace
app_name = 'api'

urlpatterns = [
    path('', docs, name='docs'),
    path('docs/', docs, name='docs'),
    path('methods/', methods, name='methods'),
    path('endpoints/', endpoints, name='endpoints'),
]

# Extend app.url patterns with those provided by router
urlpatterns += router.urls
