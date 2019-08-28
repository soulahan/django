from django.shortcuts import render
from django.http import HttpResponse  # 引入HttpResponse
# Create your views here.

# 定义indexView的动作


def index(request):
    return HttpResponse("Hello, world. You're at the api001 index.")