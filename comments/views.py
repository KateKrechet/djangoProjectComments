from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def index(req):
    films = Kino.objects.all()
    data = {'kino': films}
    return render(req, 'index.html', data)


def film(req, id):
    film = Kino.objects.get(id=id)
    forma = CommentForm()
    commentsall = film.comment_set.filter(active=True)
    if req.POST:
        commentnew = Comment.objects.create()
        commentnew.name = req.POST.get('name')
        commentnew.body = req.POST.get('body')
        commentnew.kino=film
        commentnew.save()
    data = {'forma': forma, 'commentsall': commentsall, 'kino': film}
    return render(req, 'film.html', context=data)
