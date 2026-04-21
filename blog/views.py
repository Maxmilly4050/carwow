from django.shortcuts import render
from .data.blog_posts import BLOG_POSTS
from .models import Post

def home(request):
    blog_posts = Post.objects.all()
    return render(request, "blogs/home.html", {"blog_posts": blog_posts})

def all_posts(request):
    blog_posts = Post.objects.all()
    return render(request, "blogs/all_posts.html", {"blog_posts": blog_posts})

def post(request, slug):
    try:
        blog_post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return render(request, "blogs/post_not_found.html", status=404)
    return render(request, "blogs/post.html", {"post": blog_post})

def about(request):
    return render(request, "blogs/about.html")