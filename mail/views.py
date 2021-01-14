from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.urls import reverse


def sendmail(request):
    if request.method == 'POST':
        name = request.POST['sender']
        emailsender = request.POST['email']
        message = request.POST['message']
        subject = f'Message from {name}'
        try:
            email = EmailMessage(
                subject,
                message,
                'ramkumar.dj15@gmail.com',
                ['ramkumarmani2000@gmail.com'],
                reply_to=[emailsender]
            )
            email.send()
            messages.success(request, 'Email Sent')
            print('Mail Sent')
            return HttpResponseRedirect(reverse('mail'))
        except:
            messages.error(request, 'Email not Sent')
            return HttpResponseRedirect(reverse('mail'))
    return render(request, 'mail.html')