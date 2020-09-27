from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Blog App Created</h1>")