from django.shortcuts import render
from fcm_django.models import FCMDevice


def home(request):
    if request.method == "POST":
        title = request.POST['title']
        message = request.POST['message']
        devices = FCMDevice.objects.all()
        devices.send_message(title=title, body=message)
        return render(request, 'home.html')
    return render(request, 'home.html')
