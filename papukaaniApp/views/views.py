from django.shortcuts import render

def index(request):
    return render(request, 'papukaaniApp/index.html')


def public(request):
    return render(request, 'papukaaniApp/public.html')



