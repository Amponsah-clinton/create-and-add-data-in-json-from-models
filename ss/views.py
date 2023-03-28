from django.shortcuts import render
from .models import aa
import json
from django.http import JsonResponse

# Create your views here.

def json(request):
    data = list(aa.objects.values())
    return JsonResponse(data, safe=False)