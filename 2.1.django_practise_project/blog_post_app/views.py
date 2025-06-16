from django.shortcuts import render,get_object_or_404
from . models import post
from django.views.generic import CreateView,UpdateView,DeleteView
# Create your views here.

def home(request):
    posts=post.objects.all()
    return render(request,"blog/home.html",{"posts":posts})

#view details
def post_details(request,pk):
    post=get_object_or_404(post,pk=pk)
    return render(request,"blog/post_detail.html",{"post":post})

#new post
class PostCreateview(CreateView):
    model=post
    template_name="blog/post_form.html"
    fields=["title","content"]
    success_url=reverse_lazy("home")

#update
class PostUpdateview(UpdateView):
    model=post
    template_name="blog/post_form.html" 
    fields=["title","content"]
    success_url=reverse_lazy("home")

#delete
class PostDeleteview(DeleteView):
    model=post
    template_name="blog/post_delete.html"
    success_url=reverse_lazy("home")