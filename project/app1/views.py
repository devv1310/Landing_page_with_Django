from django.shortcuts import render



# Create your views here.
from django.http import HttpResponse,JsonResponse


def index1(request):
    return HttpResponse("<h5>welcome to my app1</h5>")

# def index(request):
#     return JsonResponse("<h5>welcome to my page</h5>")