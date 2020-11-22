from django.urls import path
from .views import (
   converter, contacts
)

# url dispatcher namespace
app_name = 'converter_frontend'

urlpatterns = [
    path('', converter),
    path('contacts/', contacts),
]
