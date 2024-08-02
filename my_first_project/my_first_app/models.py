from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=20, null=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.year}"

class Publisher (models.Model):
    name = models.TextField(max_length=150)
    address =models.TextField(max_length=150)

    def __str__(self) -> str:
        return self.name

    
class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date =models.DateField()

    def __str__(self) -> str:
        return self.name
    
class Profile(models.Model):
    author =models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biografia = models.TextField(max_length=500)

    



class Book(models.Model):
    title =models.TextField(max_length=150)
    pubication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self) -> str:
        return self.title    






