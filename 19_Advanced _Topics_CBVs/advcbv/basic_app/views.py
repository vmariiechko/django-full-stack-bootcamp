from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class CBView(View):
    def get(self, request):
        return HttpResponse("Class Based Views are Cool!")