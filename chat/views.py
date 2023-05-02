from pyexpat.errors import messages
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url ='/login/')

def index(request):
    if request.method == 'POST':
        print("Received data " + request.POST['textmassage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST['textmassage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessage = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessage})

def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate (username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True,  'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})

def register_view(request): 
    redirect = request.GET.get('next')

    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            if User.objects.filter(username=request.POST['username']).exists():               
                messages.info(request, 'username is taken')
                raise forms.ValidationError(
                "password and confirm_password does not match")
         
            else:
                user= User.objects.create_user(username=request.POST['username'], password= request.POST['password'])
                user.save()
                return render(request, 'auth/login.html', {'redirect': redirect})
    
        else:
          messages.error(request, 'Password Not Match')
          raise forms.ValidationError(
            "password and confirm_password does not match")
        
    return render(request, 'auth/register.html')
 

