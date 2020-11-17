from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
# context variable value take its place in html under soname placeholder
def about(request):
    return HttpResponse(
        render_to_string(
            'about.html',
            {'description': 'Сдесь обычно стоит: Про этот сайт'}
        )
    )


def contacts(request):
    # just display word about by opening /about/ uri
    # return HttpResponse('Контактная информация')
    template = get_template('contacts.html')
    context = {'description': 'Сдесь обычно стоит: Главная Страница'}
    return HttpResponse(
        template.render(context)
    )


def converter(request):
    return render(request, 'converter.html')


def index(request):
    CONST = True

    template = Template('<h1>{{ variable }}</h1>')

    if CONST:
        context_value = {'description': 'Главная страница'}
    else:
        context_value = {'variable': 'Совсем не главная страница'}

    context = Context(context_value)

    return HttpResponse(template.render(context))


def home(request):
    template = get_template('index.html')
    context = {'description': 'Сдесь обычно стоит: Домашняя страница'}
    return HttpResponse(
        template.render(context)
    )
