from sqlite3 import dbapi2
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    db = Post.objects.all()
    context = {
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post':db,
    }

    print(request.GET);
    return render(request, 'blog/index.html', context)


def recent(request):
 return HttpResponse("ini blog")
