from django.contrib import admin
from blog.models import Author, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at", "category", "is_featured")
    prepopulated_fields = {"slug": ("title",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)



admin.site.site_header = "Carwow Blog Admin"
admin.site.site_title = "Carwow Blog Admin Portal"

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)