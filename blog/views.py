from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Artical

# Create your views here.

def home(request):
    post_list = Artical.objects.all()
    return render(request,'blog/home.html',{'post_list':post_list})

def Detail(request,id):
    try:
        post = Artical.objects.get(id=str(id))
    except Artical.DoesNotExist:
        raise Http404
    return render(request, 'blog/post.html', {'post': post})