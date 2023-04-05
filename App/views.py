from django.shortcuts import render
from App.models import *
# Create your views here.

def display_topic(request):
    LOT=Topic.objects.all()

    d={'topics':LOT}

    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    
    d={'webpages':LOW}

    return render(request,'display_webpage.html',context=d)

def display_ar(request):
    LOA=AccessRecord.objects.all()
    
    d={'accessrecord':LOA}

    return render(request,'display_ar.html',context=d)