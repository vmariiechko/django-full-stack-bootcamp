from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<em>My Second App</em>")

def help(response):
    help_dict = {"help_insert": "Help Page"}
    return render(response, "AppTwo/help.html", context=help_dict)