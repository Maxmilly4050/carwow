from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    published_at = models.DateField()
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    Category = models.CharField(max_length=50)

    def __str__(self):
        return self.Category
