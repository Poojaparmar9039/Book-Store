from django.db import models

class Book(models.Model):
    poster = models.ImageField(upload_to="posters/", null=True,blank=True)
    bookname=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.TextField()
    Bookpdf=models.FileField(upload_to="pdf", null=True,blank=True)

