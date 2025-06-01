from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def members(request):
    return HttpResponse("Hello World! This is the members page of my_jc_club.") 