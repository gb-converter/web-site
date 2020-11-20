import os
import json

from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpRequest
from django.http import HttpResponse
from django.utils.html import mark_safe


# Create your views here.
# context variable value take its place in html under soname placeholder
# def about(request):
#     return HttpResponse(
#         render_to_string(
#             'about.html',
#             {'description': 'Сдесь обычно стоит: Про этот сайт'}
#         )
#     )


def contacts(request):
    # just display word about by opening /about/ uri
    # return HttpResponse('Контактная информация')
    template = get_template('contacts.html')
    context = {
        'project_home': 'https://github.com/gb-converter?tab=projects',
        'project_components': {
            'api': 'https://github.com/gb-converter/parser',
            'parser': 'https://github.com/gb-converter/parser',
            'web': 'https://github.com/gb-converter/web-site'
        }

    }

    return HttpResponse(
        template.render(context)
    )


def converter(request):

    path = os.path.join((os.getcwd()), 'data_file.json')

    with open(path, 'r',  encoding='utf-8') as data:
        currencies_data = json.load(data)

    # Extract date from dictionary
    currencies_date = currencies_data.pop("Date")

    # Get currency info, a dict in form:
    #   "AUD": {
    #     "Цифр. код": "036",
    #     "Символ": "$",
    #     "Единица": "1",
    #     "Валюта": "Австралийский доллар",
    #     "Курс": "55,5784"
    #   }

    return render(
        request,
        'converter.html',
        {
            'currency_info': currencies_data,
            'currencies_rate_date': currencies_date
        }
    )


# def index(request):
#     CONST = True
#
#     template = Template('<h1>{{ variable }}</h1>')
#
#     if CONST:
#         context_value = {'description': 'Главная страница'}
#     else:
#         context_value = {'variable': 'Совсем не главная страница'}
#
#     context = Context(context_value)
#
#     return HttpResponse(template.render(context))


# def home(request):
#     template = get_template('index.html')
#     context = {'description': 'Сдесь обычно стоит: Домашняя страница'}
#     return HttpResponse(
#         template.render(context)
#     )
