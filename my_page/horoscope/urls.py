from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyDateConverter, 'my_date')
register_converter(converters.MyFloatConverter, 'my_float')

urlpatterns = [
    path('', views.get_index, name='horoscope-index'),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('types', views.types),
    path('types/<str:elem>', views.horoscope_element, name='horoscope-type'),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),

    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),
]
