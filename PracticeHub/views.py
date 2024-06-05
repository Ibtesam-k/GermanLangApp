from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Noun, Article
# Create your views here.

def home(request):
      return render(request,"PracticeHub/home.html")

def quiz(request):
    print("Hallo")
    ids = Noun.objects.values_list('id', flat=True)
    randomId= random.choice(ids)
    randomNoun  = Noun.objects.select_related("singular_article").get(pk = randomId)
    articles = Article.objects.all()
    print(articles)
    context = {"title":"Noun Quiz","noun":randomNoun,"articles":articles}
    return render (request, "PracticeHub/quiz.html", context)


def nouns(request):
    allNouns  = Noun.objects.select_related("singular_article").all()
    return render(request,"PracticeHub/nouns.html",{'nouns':allNouns})

