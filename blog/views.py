from django.shortcuts import render, get_object_or_404
from .models import Area, Animal, Zone, Zookeeper, Parttime, CheckLog, DetailLog
import datetime
# Create your views here.

from django.http import HttpResponse
from django.template import loader

def zindex(request):
    return render(request, "index2.html")

def manper(request, id):
    l = Zookeeper.objects.filter(id=id).values("zone_id","pt_id")
    z = Zone.objects.filter(id=l[0])
    pt = Parttime.objects.filter(id=l[1])

def reset(request):
    c = CheckLog.objects.all.values("clog_bf")