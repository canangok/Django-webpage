from django.shortcuts import render
from houseofapps.hackathon.models import Hackathon, Navigation, Sponsors, Prize, Program, Committee, Sss
from django.db.models import Count
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import locale


def starting_date(start_date):
    locale.setlocale(locale.LC_ALL, '')
    a = datetime.strftime(start_date, '%d,%B,%Y')
    date = a.split(",")
    return date



def hackathon_view(request):
    hack = Hackathon.objects.get(active=True)
    navs = Navigation.objects.filter(hackathon=hack).order_by('order')
    spons = Sponsors.objects.filter(hackathon=hack)
    prize = Prize.objects.filter(hackathon=hack).order_by('order')
    days = Program.objects.values('day').annotate(dcount=Count('day')).order_by('day')
    first_prog = Program.objects.filter(hackathon=hack, day=1).order_by('order')
    second_prog = Program.objects.filter(hackathon=hack, day=2).order_by('order')
    third_prog = Program.objects.filter(hackathon=hack, day=3).order_by('order')
    jury = Committee.objects.filter(jury=True, hackathon=hack)
    mentor = Committee.objects.filter(mentor=True, hackathon=hack)
    sss = Sss.objects.filter(hackathon=hack).order_by('order')
    return render(request, 'hackathon/index.html', {'hack': hack,
                                                    'navs': navs,
                                                    'spons': spons,
                                                    'prize': prize,
                                                    'days': days,
                                                    'first_prog': first_prog,
                                                    'second_prog': second_prog,
                                                    'third_prog': third_prog,
                                                    'jury': jury,
                                                    'mentor': mentor,
                                                    'sss': sss,
                                                    'start_date':starting_date(hack.starting_date)
                                                    })


def send_mail_hackathon(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('subject', '')
    from_email = request.POST.get('from_email', '')
    message = request.POST.get('message')

    if message is not None and message != "" and message != 'Message':
        try:
            send_mail(subject, message, from_email, ['info@houseofapps.com'])

            messages.success(request,'Mesaj gönderildi.')
            return HttpResponseRedirect('/hackathon')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/send_email')
    else:

        messages.warning(request,'Mesaj gönderilemedi.')
        return HttpResponseRedirect('/hackathon')
