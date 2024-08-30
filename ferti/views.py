from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/Home.html')


def soilAnalysis(request):
    return render(request, 'pages/soil_from.html')


def cropYield(request):
    return render(request, 'pages/cropyield.html')


def sustainability(request):
    return render(request, 'pages/sustainable.html')


def fertilizer(request):
    return render(request, 'pages/fertilizer.html')
