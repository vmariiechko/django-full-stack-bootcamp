from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    return render(request, "AppTwo/index.html")

def help(request):
    help_dict = {"help_insert": "Help Page"}
    return render(request, "AppTwo/help.html", context=help_dict)

def users(request):
    user_list = User.objects.order_by("first_name")
    user_dict = {"users": user_list}
    return render(request, "AppTwo/users.html", user_dict)