 #coding=utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def hello(request):
    return HttpResponse("Hello World!")
    

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
    
def ua_display_good2(request):#当一个特定的Header数据不存在时，给出一个优雅的回应
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)

def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('display_meta.html', {'values': values})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset,'next_time': dt})
