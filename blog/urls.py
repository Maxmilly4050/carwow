import django.urls
from . import views

urlpatterns = [
    django.urls.path('', views.home, name='home'),
    django.urls.path('post/<slug:slug>/', views.PostView.as_view(), name='post'),
    django.urls.path('post/<slug:slug>/comment/', views.CommentView.as_view(), name='comment'),
    django.urls.path('posts/', views.all_posts, name='posts'),
    django.urls.path('about/', views.AboutView.as_view(), name='about'),
    django.urls.path('favorites/', views.FavoritePostsView.as_view(), name='favorite_posts'),
]