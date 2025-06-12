from django.shortcuts import render
from . models import post
# Create your views here.

def home(request):
    posts=post.objects.all()
    return render(request,"home_page/home.html",{"posts":posts})