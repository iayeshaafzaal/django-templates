from django.shortcuts import render, HttpResponse
from home.models import Contact


# Create your views here.
def home(request):
    context = {'name': 'Harry', 'course': 'django'}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
    print(request.method)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been written to the db")
    return render(request, 'contact.html')
