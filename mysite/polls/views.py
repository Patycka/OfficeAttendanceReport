from .models import Engineer
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    latest_engineer_list = Engineer.objects.order_by('id')[:5]
    #output = ', '.join([q.name for q in latest_engineer_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_engineer_list': latest_engineer_list,
    }
    return HttpResponse(template.render(context, request))


def new_engineer(request):
    return HttpResponse("Hello, add new enginer in RA")


def my_presence(request):
    return HttpResponse("Hello, add my presence")
