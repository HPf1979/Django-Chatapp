from django.shortcuts import render
from .models import Chat, Message


def index(request):
    if request.method == 'POST':
        print("Received data " + request.POST['textmassage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST['textmassage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessage = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessage})
