from django.http import HttpResponse
from django.shortcuts import render,redirect
from . forms import MyUserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from . models import User,Task
from django.db.models import Q


# Create your views here.

def home(request):
    user=request.user
    tasks=Task.objects.filter(Q(user__email=user))
    context={'tasks':tasks}
    return render(request,'main.html',context)

def loginView(request):
    stat='login'
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=User.objects.get(email=email)
        except:
            return HttpResponse('error in email')

        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('error in logging in')
        

    context={'stat':stat}
    return render(request,'todoapp/reg_login.html',context)

def deltask(request,pk):
    task=Task.objects.get(id=pk)

    if request.user!=task.user:
        return HttpResponse('you cannot do this')

    if request.method=='POST':
        task.delete()
        return redirect('home')
    return render(request,'todoapp/delete.html',{'obj':task})

    

def logoutView(request):
    logout(request)
    return redirect('home')
    

def register(request):
    form=MyUserCreationForm()
    if request.method=='POST':
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
    context={'form':form}
    return render(request,'todoapp/reg_login.html',context)

@login_required(login_url='login')
def addtask(request):
    if request.method=='POST':
        Task.objects.create(
            user=request.user,
            task=request.POST.get('task'),

        )
        return redirect('home')

    return render(request,'todoapp/addtask.html')