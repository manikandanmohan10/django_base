from django.urls import path

from .views import encode, utc_timezone, txt, safest, module_load, date_parse, d_decorator

urlpatterns = [
    path('encoding/', encode, name='encode'),
    path('utc_timezone/', utc_timezone, name='utc_timezone'),
    path('txt/', txt, name='txt'),
    path('safestring/', safest, name= 'safestring' ),
    path('module_load/', module_load, name = 'module_load'),
    path('date_parse/', date_parse, name='date_parse'),
    path('d_decorator', d_decorator, name = 'd_decorator'),
]