from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {"insert_me": "Hello, I'm from first_app!"}
    return render(request, "first_app/index.html", context=my_dict)