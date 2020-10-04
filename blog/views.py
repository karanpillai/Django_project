from django.shortcuts import render,HttpResponse
from .models import Post
posts = [
    {
        'author':'Karan',
        'title': 'Blog post 1',
        'description':'My first blog',
        'date': 'September 27,2020'
    },
    {
        'author':'Arjun',
        'title': 'Blog post 2',
        'description':'My Second blog',
        'date': 'September 29,2020'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html',{"title":"About"})

    