from django.contrib import admin
from blog.models import Author, Category, Comment, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at", "category", "is_featured")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("category", "author", "published_at", "is_featured")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("Category",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "post", "created_at")
    list_filter = ("created_at",)



admin.site.site_header = "Carwow Blog Admin"
admin.site.site_title = "Carwow Blog Admin Portal"

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)