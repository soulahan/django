import json
from django.shortcuts import render
from django.http import HttpResponse
from api.models import Trip
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the trips index.")


def tripList(request):
    all_objs = Trip.objects.get(pk=1)
    all_dicts = Trip.toDict(all_objs)
    all_jsons = json.dumps(all_dicts)
    return HttpResponse(all_jsons)


def tripDetail(request, trip_id):
    return HttpResponse("This is the view for tripDetail %s." % trip_id)


def tripDayDetail(request, trip_id, day_id):
    return HttpResponse("This is the view for tripDayDetail %s-%s." % (trip_id,day_id))
