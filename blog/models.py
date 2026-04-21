from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300)
    author = models.CharField(max_length=100)
    published_at = models.DateField()
    content = models.TextField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
