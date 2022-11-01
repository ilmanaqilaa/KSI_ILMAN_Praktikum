from django.http import HttpResponse

def articles(request, year):
    year = year
    str = year
    return HttpResponse(year)

def index(request):
    return HttpResponse("ini index")

def about(request):
    return HttpResponse("ini about")