from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    context = {'name': 'Harry', 'course': 'django'}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
    return render(request, 'contact.html')
