from django.shortcuts import render
from .models import Message


def index(request):
    if request.method == 'POST':
        print("Received data " + request.POST['textmassage'])

        Message.objects.create(
            text=request.POST['textmassage'], chat=None, author=request.user, receiver=request.user)
        return render(request, 'chat/index.html', {'username': 'Herlina'})
