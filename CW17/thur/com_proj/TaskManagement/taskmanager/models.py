from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    DEFAULT_CATEGORY = Category(name="None")
    STATUS_CHOICES = (
        ('d', 'Done'),
        ('t', 'To Do'),
        ('dnf', 'Did Not Finish'),
    )

    author = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
