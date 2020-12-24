from django.urls import path
from .views import (
   converter, contacts, converter_edit
)

# url dispatcher namespace
app_name = 'converter_frontend'

urlpatterns = [
    path('', converter, name='converter'),
    path('contacts/', contacts, name='contacts'),
    path('^ajax/get_response/$', converter_edit, name='get_response')
]