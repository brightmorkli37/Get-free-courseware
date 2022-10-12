from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

def index(request):

    template_name = 'courses_app/index.html'
    context = {}
    return render(request, template_name, context)


def send_mail(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    courses = request.POST.get('courses')

    template = loader.get_template('courses_app/email_message.txt')
    context = {
        'name': name,
        'email': email,
        'courses': courses,
    }

    message = template.render(context)

    email = EmailMultiAlternatives(
        'TechJuice Courses', message,
        "Congratulations " + "- a gift for you",
        ["brightmorkli37@gmail.com", email]
    )

    # convert email_message.txt to html
    email.content_subtype = "html"
    email.send()
    messages.success(request, 'We sent a link to your email')
    return HttpResponseRedirect('/')
