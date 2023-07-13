from django.db import models

# Create your models here.

class Post(models.Model):
    STATUS_CHOISES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOISES, max_length=3)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

