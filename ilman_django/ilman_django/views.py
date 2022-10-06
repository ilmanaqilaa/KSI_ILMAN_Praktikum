from django.http import HttpResponse

def index(request):
    return HttpResponse("ini index")

def about(request):
    return HttpResponse("ini about")