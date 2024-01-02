from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)

    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=30)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True )
    content = models.CharField("Post Content", max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts") 

    def __str__(self):
        return f" {self.title}"

class Tag(models.Model):
    caption = models.CharField(max_length=30)
    address = models.OneToOneField(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f" {self.caption}"