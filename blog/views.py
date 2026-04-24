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

class PostView(View):
    def get(self, request, slug):
        try:
            blog_post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return render(request, "blogs/post_not_found.html", status=404)
        
        comments = Comment.objects.filter(post=blog_post)
        form = CommentForm()
        return render(request, "blogs/post.html", {
            "post": blog_post,
            "comments": comments,
            "form": form,
        })
    def post(self, request, slug):
        try:
            blog_post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return render(request, "blogs/post_not_found.html", status=404)
        
        favorite_posts = request.session.get("favorite_posts", [])
        if blog_post.pk in favorite_posts:
            favorite_posts.remove(blog_post.pk)
        else:
            favorite_posts.append(blog_post.pk)
        request.session["favorite_posts"] = favorite_posts
        
        return redirect('post', slug=slug)

# def post(request, slug):
#     try:
#         blog_post = Post.objects.get(slug=slug)
#     except Post.DoesNotExist:
#         return render(request, "blogs/post_not_found.html", status=404)
    
#     saved_posts = []
#     favorite_post = request.session.get("favorite_post")
#     if favorite_post == None or favorite_post.length == 0:
#         favorite_post = saved_posts
#     else:
#         favorite_post = Post.objects.get(slug=blog_post.slug)
#         saved_posts.append(int(favorite_post.pk))
#         favorite_post = saved_posts
    
#     comments = Comment.objects.filter(post=blog_post)
#     form = CommentForm()
#     return render(request, "blogs/post.html", {
#         "post": blog_post,
#         "comments": comments,
#         "form": form,
#     })


class AboutView(TemplateView):
    template_name = "blogs/about.html"

class FavoritePostsView(View):
    def get(self, request):
        favorite_posts = request.session.get("favorite_posts")
        to_be_loaded_posts = Post.objects.filter(pk__in=favorite_posts)
        return render(request, "blogs/favorite_posts.html", {"favorite_posts": to_be_loaded_posts})