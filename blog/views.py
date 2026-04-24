from urllib import request
from django.shortcuts import redirect, render
from .data.blog_posts import BLOG_POSTS
from .models import Post, Comment
from .forms import CommentForm
from django.views import View
from django.views.generic import TemplateView

class CommentView(View):
    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(slug=slug)
            comment.save()
            return redirect('post', slug=slug)
        else:
            return render(request, "blogs/comment_form.html", {"form": form, "slug": slug})
        

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
    
    saved_posts = []
    favorite_post = request.session.get("favorite_post")
    if favorite_post == None or favorite_post.length == 0:
        favorite_post = saved_posts
    else:
        favorite_post = Post.objects.get(slug=blog_post.slug)
        saved_posts.append(int(favorite_post.pk))
        favorite_post = saved_posts
    
    comments = Comment.objects.filter(post=blog_post)
    form = CommentForm()
    return render(request, "blogs/post.html", {
        "post": blog_post,
        "comments": comments,
        "form": form,
    })


class AboutView(TemplateView):
    template_name = "blogs/about.html"

class FavoritePostsView(View):
    def get(self, request):
        favorite_posts = Post.objects.filter(is_favorite=True)
        return render(request, "blogs/favorite_posts.html", {"favorite_posts": favorite_posts})