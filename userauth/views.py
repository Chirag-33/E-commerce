from django.shortcuts import render,redirect
from . forms import CreateUserForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have succesfully signed up')
        return redirect('userauth:login_view')
    context = {
        'form': form
    }
    
    return render(request, 'userauth/register.html', context)

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user =authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request, 'You have successfully logged in')
                return redirect('core:index')
        

            else:
                messages.warning(request,'Invalid email or password')
        else:
            messages.error(request,'form is not valid')
    
    context = {
        'form': form
    }
    return render(request, 'userauth/login.html', context)
        

def logout_view(request):
    logout(request)
    messages.success(request,'you have successfully logged out')
    return redirect('userauth:login_view')

