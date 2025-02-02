from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def homePageView(request):
#     return HttpResponse("Hello, World!")

class HomePageView(TemplateView):
    template_name = "homepage.html"

class AboutPageView(TemplateView):
    template_name = "about.html"