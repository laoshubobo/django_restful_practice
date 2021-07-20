from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

def doSpecialmath(n):
    if n < 2:
        return n
    p1 = 0
    p2 = 1
    res = 0
    for cur in range(2, n + 1):
        res = cur + p1 + p2
        p1 = p2
        p2 = res
    return res

def specialmath(request, number):
    if request.method == 'GET':
            try:
                res = doSpecialmath(int(number))
                response = json.dumps([{'special math result:': str(res)}])
            except:
                response = json.dumps([{'Error': 'Not a number'}])
    return HttpResponse(response, content_type='text/json')