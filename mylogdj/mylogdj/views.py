from django.shortcuts import render,redirect
from django.contrib import auth 
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def home(request):
    #这里content必须是字典形式才能返回
    content = {}
    return render(request,'home.html',content)

@csrf_exempt
def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    if user is not None:
        auth.login(request, user)
        return redirect(referer)
    else:
        return render(request,'error.html',{'message':'用户名或密码不正确'})