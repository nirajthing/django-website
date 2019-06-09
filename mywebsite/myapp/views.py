from django.shortcuts import render

# Create your views here.
def mywebsite(request):
    return render(request, 'mainpage.html')