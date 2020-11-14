from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def converter(request):
    return render(request, 'converter.html')


def about(request):
    return render(request, 'about.html')
