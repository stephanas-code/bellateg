from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    submitted = False
    if request.POST:
        form = ContactForm(request.POST)
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']

        if form.is_valid():
            """
            send_mail(
                f'Sub: {subject}' , #title
               f'Dear {name}, if you are receiving this mail, you have successfully received your submission. We are glad that you have decide to use our services. A member of the support team will reply your and help solve the issue(s). Responses takes 4 to 8 hours.\
               \
                 Thank you.\
                 \
                 Stephanas Odogu.\
                 \
                 Chief Executive Officer , ', # message
                settings.EMAIL_HOST_USER,
                [ email, 'stephanas.odogu@cybria.tech'],#receivers email
                fail_silently=False
                

            )
            """
            form.save()

            return HttpResponseRedirect("/?submitted=True")
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, "hairmpire/index.html",{
        'form' : ContactForm(),
        "submitted" : submitted
    })


def about(request):
    return render(request, 'hairmpire/about.html')

def services(request):
    return render(request, 'hairmpire/services.html')

def contact(request):
    submitted = False
    if request.POST:
        form = ContactForm(request.POST)
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']

        if form.is_valid():
            """
            send_mail(
                f'Sub: {subject}' , #title
               f'Dear {name}, if you are receiving this mail, you have successfully received your submission. We are glad that you have decide to use our services. A member of the support team will reply your and help solve the issue(s). Responses takes 4 to 8 hours.\
               \
                 Thank you.\
                 \
                 Stephanas Odogu.\
                 \
                 Chief Executive Officer , ', # message
                settings.EMAIL_HOST_USER,
                [ email, 'stephanas.odogu@cybria.tech'],#receivers email
                fail_silently=False
                

            )
            """
            form.save()

            return HttpResponseRedirect("/contact?submitted=True")
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    
    

    return render(request, 'hairmpire/contact.html',{
        'form' : ContactForm(),
        "submitted" : submitted
    })