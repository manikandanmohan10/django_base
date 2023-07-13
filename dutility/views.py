from django.shortcuts import render
from django.utils import encoding as e
from django.utils import timezone as tz
from datetime import datetime, timezone
from django.http import HttpResponse, JsonResponse
import pytz
import json
from django.utils import text as t
from django.utils import safestring as s
from django.utils.module_loading import import_string
from django.utils import dateparse as dp
# encoding


def encode(request):
    str_encode = e.smart_str("encode", encoding='utf-8', strings_only=True, errors='strict')
    # convert to unicode string and encoded as byte string.
    # it ensure that string are properly encoded for use in django.
    encode_false = e.smart_str(False, encoding='utf-8', strings_only=False, errors='strict')
    encode_without_string_only = e.smart_str(False, encoding='utf-8', strings_only=True, errors='strict')

    # to check object is protected type
    e.is_protected_type('s')
    # strict than the smart_str even convert byte string to byte string
    e.force_str('stri')
    return HttpResponse(f"{str_encode}</br>{encode_false} {type(encode_false)}</br>{encode_without_string_only} {type(encode_without_string_only)}")

# timezone

def utc_timezone(request):
    response = {}
    # utc = tz.utc()
    # fix_tz = tz.get_fixed_timezone()
    response['default_tz'] = str(tz.get_default_timezone())
    print(response['default_tz'])
    response['default_tz_name'] = tz.get_default_timezone_name()
    print(response['default_tz_name'])
    response['cur_timezone'] = str(tz.get_current_timezone())
    print(response['cur_timezone'])
    response['cur_tz_name'] = tz.get_current_timezone_name()
    print(response['cur_tz_name'])
    # install tzdata
    tz.activate('Asia/Calcutta')
    response['after_activate_default_tz'] = tz.get_default_timezone_name()
    response['after_activate_cur_tz'] = tz.get_current_timezone_name()
    tz.deactivate()
    response['after_deactivate_cur_tz'] = tz.get_current_timezone_name()

    # tz.override('Asia/Calcutta')
    dt = datetime(2020, 1, 1)
    dt_aware = dt.astimezone(timezone.utc)
    response['initial_datetime_obj'] = dt_aware.isoformat()
    dt_aware = tz.localtime(dt_aware, pytz.timezone('Asia/Calcutta'))
    response['after_set_localtime_datetime_obj'] = dt_aware.isoformat()
    response['after_set_localtime_to_none_datetime_obj']  = tz.localtime(dt_aware, None).isoformat()
    response['local_date'] = tz.localdate(value=dt_aware, timezone=pytz.timezone('Asia/Calcutta')).isoformat()
    # CHANGE USE_TZ in setting
    tz.activate('Asia/Calcutta')
    # print(tz.now())
    # check datetime is not naive
    response['datetime_is_aware'] = tz.is_aware(datetime(2019, 12, 2))
    response['datetime_with_tz_is_aware'] = tz.is_aware(dt_aware)
    response['datetime_with_tz_is_naive'] = tz.is_naive(dt_aware)
    response['datetime_is_naive'] = tz.is_naive(datetime(2022, 3,3))
    
    # tz.make_aware(dt_aware, timezone='Asia/Calcutta', is_dst=None)
    response['datetime_with_tz_to_only_datetime'] = tz.make_naive(dt_aware, timezone=None).isoformat()
    return JsonResponse(response)


def txt(request):
    name = 'keerthana'
    age = 21
    response = {}
    response['message'] = t.format_lazy('{} is {} years old', name, age)
    # lazy object
    # string to be translated only when it is needed.(rendered)

    response['s_str'] = t.slugify('  aRt is Life', allow_unicode = False)
    response['s_str2'] = t.slugify('你好 World', allow_unicode=True)
    return JsonResponse(response)

def safest(request):
    response = {}
    response['message'] = s.mark_safe('<b> hello world</b>   ')
    type(response['message'])
    # returned object can be used every where a string
    # can be clled multiple times on a single tring

    # can also be used as a decorator
    response['unsafe_string'] =  response['message'].strip()
    type(response['unsafe_string'])

    return JsonResponse(response)

def module_load(request):
    ValidationError = import_string('django.core.exceptions.ValidationError')

    # from django.core.exceptions import ValidationError
    print(ValidationError)
    return JsonResponse({'v': 'hello'})


def date_parse(request):
    response = {}
    response['dateparse'] = dp.parse_date('2019-01-01').isoformat()
    response['timeparse'] = dp.parse_time('12:00').isoformat()
    response['datetime'] = dp.parse_datetime("2022-01-01T12:00:00").isoformat()
    response['datetime2'] = dp.parse_datetime("2022-01-01 12:00:00").isoformat()
    
    response['duration'] = dp.parse_duration("2:30")
    # dp.parse_datetime("January 1, 2022 12:00:00")
    return JsonResponse(response)


def d_decorator(request):
    pass