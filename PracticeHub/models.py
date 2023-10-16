from django.db import models

# Create your models here.
class Article (models.Model):
    name = models.CharField(max_length=10,unique=True)
    color = models.CharField(max_length=15)

    def __str__(self) -> str:
        return  self.name+"("+self.color+")"



class Noun (models.Model):
    name = models.CharField(max_length=50,unique=True)
    plural = models.CharField(max_length=75)
    plural_abbr = models.CharField(max_length=50)
    singular_article = models.ForeignKey(Article, on_delete=models.PROTECT) #SET_NULL

    def __str__(self) -> str:
        return self.singular_article.name+" "+self.name+" ,"+self.plural_abbr+"=> die "+self.plural

