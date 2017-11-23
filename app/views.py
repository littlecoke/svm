# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from app.forms import ApiForm
from libs.svm import *


@csrf_exempt
def api(request):
    if request.method != "POST":
        message = dict()
        message['result'] = "invalid request method"
        message['isSuccess'] = False
        return JsonResponse(message)
    form = ApiForm(request.POST)
    if form.is_valid():
        key = form.cleaned_data["key"]
        result = predict_API(key)
        message = dict()
        message['result'] = result
        message['isSuccess'] = True
        return JsonResponse(message)
    message = dict()
    message['result'] = "invalid form"
    message['isSuccess'] = False
    return JsonResponse(message)


