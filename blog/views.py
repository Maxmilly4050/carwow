from django.shortcuts import render
from .data.blog_posts import BLOG_POSTS

def home(request):
    return render(request, "blogs/home.html", {"blog_posts": BLOG_POSTS})