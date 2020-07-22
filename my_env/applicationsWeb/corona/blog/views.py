from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.


def all_posts(request):
    posts=Blog.objects.filter(acitve=True)
    context={
       'posts':posts
    }
    return render(request, 'blog/all_posts.html', context)



def post(request , titre):
    #post= Post.objects.get(id= id)
    post= get_object_or_404(Post , titre =titre)
    context ={
        'post' : post,
    }

    return render(request, 'blog/details.html' ,context)


def post(request , id):
    #post= Post.objects.get(id= id)
    post= get_object_or_404(Blog , id =id)
    context ={
        'post' : post,
    }

    return render(request, 'blog/details.html' ,context)
