from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Noun
# Create your views here.

def home(request):
    return HttpResponse("welcome")



def guess_article (request):
    msg = ""
    if request.method == 'POST':
        print('hi')
        answer = request.POST.get('article')
        nounId = request.POST.get('noun')
        randomNoun = Noun.objects.select_related("singular_article").get(pk = nounId)
        if randomNoun.singular_article.name == answer :
            msg = "correct"
        else:
            msg = "false"
        print(answer)
    else :
        
        ids = Noun.objects.values_list('id', flat=True)
        randomId= random.choice(ids)
        randomNoun  = Noun.objects.get(pk = randomId)
        print(randomNoun)
    return render(request,"guess.html",{'noun':randomNoun,'msg':msg})