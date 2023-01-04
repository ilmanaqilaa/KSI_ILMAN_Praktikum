from sqlite3 import dbapi2
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect

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

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return HttpResponseRedirect('/blog/')

def update(request, id):
    updt = Post.objects.get(id=id)
    data = {
        'title' : updt.title,
        'body'  : updt.body,
        'email' : updt.email,
    }
    classform = forms.classform(request.POST or None, initial=data, instance=updt)

    if request.method =='POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/blog/')

    context = {
        'heading':'Updt',
        'classform':classform
    }
    return render(request, 'form.html', context)