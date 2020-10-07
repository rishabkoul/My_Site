from django.shortcuts import render
from django.core.mail import send_mail
from . import models


def home(request):
    resume = models.Resume.objects.get(mail='rishabkoul2001@gmail.com')
    educations = models.Education.objects.all()
    skills = models.Skills.objects.all()
    context = {
        "resume": resume,
        "educations": educations,
        "skills": skills
    }
    return render(request, template_name='my_resume/home.html', context=context)


def projects(request):
    resume = models.Resume.objects.get(mail='rishabkoul2001@gmail.com')
    projects = models.Project.objects.all()
    context = {
        "resume": resume,
        "projects": projects
    }
    return render(request, template_name='my_resume/projects.html', context=context)


def achievements(request):
    resume = models.Resume.objects.get(mail='rishabkoul2001@gmail.com')
    achievements = models.Achievements.objects.all()
    context = {
        "achievements": achievements,
        "resume": resume
    }
    return render(request, template_name='my_resume/achievements.html', context=context)


def ContactCreateView(request, format=None):
    resume = models.Resume.objects.get(mail='rishabkoul2001@gmail.com')
    data = request.POST

    try:
        send_mail(
            data['subject'],
            'Name: '
            + data['name']
            + '\nEmail: '
            + data['email']
            + '\n\nMessage:\n'
            + data['message'],
            'rishabkoul2001@gmail.com',
            ['rishabkoul2001@gmail.com'],
            fail_silently=False
        )

        contact = models.Contact(
            name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
        contact.save()

        return render(request, template_name='my_resume/contact.html', context={'success': "Message sent successfully", 'resume': resume})

    except:
        return render(request, template_name='my_resume/contact.html', context={'error': "Message failed to send", 'resume': resume})


def contact(request):
    resume = models.Resume.objects.get(mail='rishabkoul2001@gmail.com')
    context = {
        "resume": resume
    }
    return render(request, template_name='my_resume/contact.html', context=context)
