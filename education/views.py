from django.shortcuts import render


# Create your views here.

def learn(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def courses(request):
    return render(request, 'courses.html')
