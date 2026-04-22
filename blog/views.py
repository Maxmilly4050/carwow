from urllib import request
from django.shortcuts import redirect, render
from .data.blog_posts import BLOG_POSTS
from .models import Post
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
    
    comments = blog_post.comments.all()
    form = CommentForm()
    return render(request, "blogs/post.html", {
        "post": blog_post,
        "comments": comments,
        "form": form,
    })

# def about(request):
#     return render(request, "blogs/about.html")
class AboutView(TemplateView):
    template_name = "blogs/about.html"