from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
from AppTwo.models import User
from . import forms

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

def sign_up(request):
    user_form = forms.UserForm()

    if request.method == "POST":
        user_form = forms.UserForm(request.POST)

        if user_form.is_valid():
            user_form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")

    return render(request, "AppTwo/sign_up.html", {"user_form": user_form})
