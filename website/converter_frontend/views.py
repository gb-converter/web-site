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


def converter(request):

    from_currency = request.POST['from_currency']

    amount_of_currency_from = float(request.POST['amount_of_currency_from'])

    to_currency = request.POST['to_currency']

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

    # Парсим json
    for key, val in currencies_data.items():
        if type(val) == str:
            continue
        elif key == from_currency:
            f_currency = float(val['Курс'].replace(',', '.'))
            if val.get('Символ') is None:
                f_symbol = 'None'
            else:
                f_symbol = val['Символ']
        elif key == to_currency:
            t_currency = float(val['Курс'].replace(',', '.'))
            if val.get('Символ') is None:
                t_symbol = 'None'
            else:
                t_symbol = val['Символ']

    if from_currency == to_currency:
        culc_result = amount_of_currency_from
        symbol = f_symbol
    else:
        culc_result = round((f_currency * amount_of_currency_from) / t_currency, 4)
        symbol = t_symbol


    # Extract date from dictionary
    currencies_date = currencies_data.pop("Date")

    # Get currency info, a dict in form:
    #   "AUD": {
    #     "Цифр. код": "036",
    #     "Символ": "$",
    #     "Единица": "1",
    #     "Валюта": "Австралийский доллар",
    #     "Курс": "55,5784"
    #   },

    return render(
        request,
        'converter_frontend/converter.html',
        {
            'currency_info': currencies_data,
            'currencies_rate_date': currencies_date,
            'converter': culc_result,
            'symbol': symbol
        }
    )
