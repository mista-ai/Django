from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

elements_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

month_dict = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date_sign_dict = {
    (3, 21, 4, 20): 'aries',
    (4, 21, 5, 21): 'taurus',
    (5, 22, 6, 21): 'gemini',
    (6, 22, 7, 22): 'cancer',
    (7, 23, 8, 21): 'leo',
    (8, 22, 9, 23): 'virgo',
    (9, 24, 10, 23): 'libra',
    (10, 24, 11, 22): 'scorpio',
    (11, 23, 12, 22): 'sagittarius',
    (12, 23, 1, 20): 'capricorn',
    (1, 21, 2, 19): 'aquarius',
    (2, 20, 3, 20): 'pisces'
}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4-х цифр - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')


def get_index(request):
    zodiacs = list(zodiac_dict)
    # f'<li><a href="{redirect_path}">{sign.title()}</a></li>'
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': [],
    }
    return render(request, 'horoscope/index.html', context=context)


def types(request):
    elements = list(elements_dict)
    li_elements = ''
    for element in elements:
        redirect_path = (reverse('horoscope-type', args=(element,)))
        li_elements += f'<li><a href="{redirect_path}">{element.title()}</a></li>'
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def horoscope_element(request, elem):
    zodiacs = elements_dict[elem]
    li_elements = ''
    for sign in zodiacs:
        redirect_path = (reverse('horoscope-name', args=(sign,)))
        li_elements += f'<li><a href="{redirect_path}">{sign.title()}</a></li>'
    response = f"""
        <ul>
            {li_elements}
        </ul>
        """
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
    }
    return render(request, template_name='horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = tuple(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = (reverse('horoscope-name', args=(name_zodiac,)))
    return HttpResponseRedirect(f'{redirect_url}')


def get_info_by_date(request, month, day):
    max_days = month_dict[month - 1] if 1 < month < 12 else 31
    if month > 12 or month < 1 or day > max_days or day < 1:
        return HttpResponseNotFound(f"Неверные месяц и день - {month}/{day}")
    for key, sign in date_sign_dict.items():
        month_from, day_from, month_to, day_to = key
        if (month_from == month and day >= day_from) or (month_to == month and day <= day_to):
            redirect_url = (reverse('horoscope-name', args=(sign,)))
            return HttpResponseRedirect(f'{redirect_url}')
    return HttpResponseNotFound(f"Что-то пошло не так - {month}/{day}")
