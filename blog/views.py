from django.shortcuts import render
from .data.blog_posts import BLOG_POSTS

def home(request):
    return render(request, "blogs/home.html", {"blog_posts": BLOG_POSTS})

def all_posts(request):
    return render(request, "blogs/all_posts.html", {"blog_posts": BLOG_POSTS})

def post(request, slug):
    blog_post = next((post for post in BLOG_POSTS if post["slug"] == slug), None)
    if blog_post is None:
        return render(request, "blogs/post_not_found.html", status=404)
    return render(request, "blogs/post.html", {"post": blog_post})

def about(request):
    return render(request, "blogs/about.html")