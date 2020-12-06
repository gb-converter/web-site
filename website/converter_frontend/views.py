import os
import json

from django.shortcuts import render
from datetime import datetime
from loguru import logger

logger.add('logg.txt', encoding='UTF-8', format="\n{time} {level} {message}", level="INFO")


def contacts(request):
    return render(
        request,
        'converter_frontend/contacts.html',
        {
            'project_components': {
                'Домашняя страница проекта': 'https://github.com/gb-converter?tab=projects',
                'Репозиторий компонента апи': 'https://github.com/gb-converter/api',
                'Репозиторий компонента парсер': 'https://github.com/gb-converter/parser',
                'Репозиторий компонента веб сайт': 'https://github.com/gb-converter/web-site'
            }
        }
    )


def parse_json():

    path = os.path.join((os.getcwd()), 'data_file.json')

    # first check if we have datafile, and download if it is not present
    # ignore errors if any
    if not os.path.isfile(path):
        try:
            os.system(f'python parser.py --path {os.getcwd()}')
        except OSError:
            pass

    # now try to extract data from downloaded file if it was created,
    # if data is unreadable or still no file, form dumb dictionary:
    try:
        with open(path, 'r',  encoding='utf-8') as data:
            currencies_data = json.load(data)
    except (json.JSONDecodeError, FileNotFoundError):
        logger.error(f'Ошибка Json файла')
        currencies_data = {
            "Date": datetime.now().date().strftime("%d.%m.%Y"),
            "Недоступно": {
                "Цифр. код": "000",
                "Символ": "",
                "Единица": "1",
                "Валюта": "Недоступно",
                "Курс": "1,0000"
            }
        }

    # Extract date from dictionary
    # currencies_date = currencies_data.pop("Date")

    # Get currency info, a dict in form:
    #   "AUD": {
    #     "Цифр. код": "036",
    #     "Символ": "$",
    #     "Единица": "1",
    #     "Валюта": "Австралийский доллар",
    #     "Курс": "55,5784"
    #   },
    return currencies_data


def converter(request):

    currencies_data = parse_json()
    currencies_date = parse_json().pop("Date")

    f_currency =  0;
    t_currency = 0;

    from_currency = request.POST.get('from_currency', False)
    amount_of_currency_from = abs(float(request.POST.get('amount_of_currency_from', False)))
    to_currency = request.POST.get('to_currency', False)

    if from_currency and amount_of_currency_from and to_currency is not False:

        for key, val in currencies_data.items():
            if type(val) == str:
                continue

            elif key == from_currency:

                if float(val['Единица']) > 1:
                    f_currency = float(val['Курс'].replace(',', '.')) / float(val['Единица'])
                else:
                    f_currency = float(val['Курс'].replace(',', '.'))

            elif key == to_currency:

                if float(val['Единица']) > 1:
                    t_currency = float(val['Курс'].replace(',', '.')) / float(val['Единица'])
                else:
                    t_currency = float(val['Курс'].replace(',', '.'))

    if from_currency == to_currency:
        culc_result = amount_of_currency_from
    else:
        culc_result = round((f_currency * amount_of_currency_from) / t_currency, 4)

    context = {
        'currency_info': currencies_data,
        'currencies_rate_date': currencies_date,
        'converter': culc_result
    }

    return render(request, 'converter_frontend/converter.html', context)
