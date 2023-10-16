from django.db import models

# Create your models here.
class Article (models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=15)



class Noun (models.Model):
    name = models.CharField()
    plural = models.CharField()
    plural_abbr = models.CharField()
    singular_article = models.ForeignKey(Article, on_delete=models.PROTECT) #SET_NULL

