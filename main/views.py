from django.shortcuts import render
from django.utils import timezone
from houseofapps.main.models import App
from PIL import Image
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def home(request):
    apps=App.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
    return render(request, 'main/index.html', {'apps':apps})

def send_email(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('subject', '')
    from_email = request.POST.get('from_email', '')
    message = request.POST.get('message')

    if message is not None and message != "" and message != 'Message':
        try:
            send_mail(subject, message, from_email, ['canangok186@gmail.com'])

            messages.success(request,'Mesaj gönderildi')
            return HttpResponseRedirect('/')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/send_email')
    else:

        messages.warning(request,'mesaj gönderilemedi')
        return HttpResponseRedirect('/')
