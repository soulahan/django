from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the trips index.")


def tripList(request):
    return HttpResponse("This is the view for tripList")


def tripDetail(request, trip_id):
    return HttpResponse("This is the view for tripDetail %s." % trip_id)


def tripDayDetail(request, trip_id, day_id):
    return HttpResponse("This is the view for tripDayDetail %s-%s." % (trip_id,day_id))
