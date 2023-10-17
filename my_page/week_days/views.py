from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

weekday_dict = {
    'monday': 'Понедельник: 1. Поучиться\n2. Поработать\n3. Поучиться\n4. Посмотреть Ван Пис 5. Поспать',
    'tuesday': 'Вторник: 1. Поучиться\n2. Поработать\n3. Поучиться\n4. Посмотреть Ван Пис 5. Поспать',
    'wednesday': 'Среда: 1. Поучиться\n2. Поработать\n3. Поучиться\n4. Посмотреть Ван Пис 5. Поспать',
    'thursday': 'Четверг: 1. Поучиться\n2. Поработать\n3. Поучиться\n4. Посмотреть Ван Пис 5. Поспать',
    'friday': 'Пятница: 1. Поучиться\n2. Поработать\n3. Поучиться\n4. Посмотреть Ван Пис 5. Поспать',
    'saturday': 'Суббота: 1. Поучиться\n2. Поработать\n3. Поучиться\n4. Посмотреть Ван Пис 5. Поспать',
    'sunday': 'Пятница: 1. Поучиться\n2. Поработать\n3. Поучиться\n4. Посмотреть Ван Пис 5. Поспать',
}


def get_index(request):
    return render(request, 'week_days/greeting.html')


# Create your views here.
def get_weekday_by_str(request, weekday):
    if weekday in weekday_dict:
        return HttpResponse(weekday_dict[weekday])
    else:
        return HttpResponseNotFound(f'There is no such weekday - {weekday}')


def get_weekday_by_number(request, weekday):
    if 1 <= weekday <= 7:
        day = tuple(weekday_dict)[weekday - 1]
        redirect_url = (reverse('todo-name', args=[day]))
        return redirect(f'{redirect_url}')
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {weekday}')
