from django.db import models

# Create your models here.
class Article (models.Model):
    name = models.CharField(max_length=10,unique=True)
    color = models.CharField(max_length=15)
    abbr = models.CharField(max_length = 3, null = True, blank = True)
    def __str__(self) -> str:
        return  self.name+"("+self.color+")"



class Noun (models.Model):
    name = models.CharField(max_length=100,unique=True)
    plural = models.CharField(max_length=75)
    plural_abbr = models.CharField(max_length=50)
    meaning = models.CharField(max_length=75,null=True)
    singular_article = models.ForeignKey(Article, on_delete=models.PROTECT) #SET_NULL
    tags = models.TextField(null=True, blank = True)
    examples = models.TextField(null= True, blank = True)

    def __str__(self) -> str:
        presentation = self.singular_article.abbr+" "+self.name+", "+self.plural_abbr
        if (self.plural != "No Plural"):   
           presentation+="=> die "+self.plural
        if self.meaning:
            presentation +=" ("+self.meaning+")"
        return presentation


class Verb(models.Model):
    verb = models.CharField(max_length=100,unique=True)
    akk = models.BooleanField()
    note = models.CharField(max_length=50)
    meaning = models.CharField(max_length=75,null=True)
    perfect_verb = models.CharField(max_length =10, null = True)
    perfect_form =models.CharField(max_length = 100, null = True)
    def __str__(self) -> str:
        kasus = ""
        if(self.akk):
            kasus = "akk"
        return self.verb+" (v)("+kasus+")("+self.note+")"