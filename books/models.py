from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField("birth day")
    biography =models.TextField(null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    synopsis = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title