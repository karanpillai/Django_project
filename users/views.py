from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm -> Django built in register form
from django.contrib import messages
from .forms import UserRegister
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! Please Login now')
            return redirect('login')
    else:    
        form = UserRegister()
    return render(request,'users/register.html',{'form':form})

@login_required # user cant access the url directly . he should first login. also add login url in settings.py file
def profile(request):
    return render(request,'users/profile.html')