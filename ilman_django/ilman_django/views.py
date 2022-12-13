from django.shortcuts import render
from django.http import HttpResponse

def articles(request, year):
    year = year
    str = year
    return HttpResponse(year)

def index(request):
    context = {
        'heading':'Form Manual'
    }

    if request.method == 'POST':
        print("ini adalah method post")
        context['username'] = request.POST['username']
        context['address'] = request.POST['address']
    else:
        print("ini adalah method GET")
    return render(request, 'index.html', context)