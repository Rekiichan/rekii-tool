from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

from . import models
from . import const_name


def home(request):
    context = {
        'element_type': const_name.ELEMENT_TYPE,
        'action_type': const_name.ACTION_TYPE,
    }
    return render(request, "home.html", context)


def process(request):
    if request.method == 'POST':
        print(81264918276487)
        return HttpResponse('asd')
    else:
        print(2735982674598)
        return HttpResponse('asd')


def process_ele_type(request, param):
    if request.method == 'GET':
        if param == 'redirect':
            return HttpResponse('3')
        return HttpResponse('4')
    else:
        return HttpResponse('NOT GET METHOD REQUEST')
