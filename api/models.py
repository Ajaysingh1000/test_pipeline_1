from django.db import models

# Create your models here.
# from pgvector.django import VectorField


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    description = models.TextField()
    publication_year = models.IntegerField()
 
    def __str__(self):
        return self.title


# class Document(models.Model):
#     content = models.TextField()
#     embedding = VectorField(dimensions=768)
