from django.shortcuts import render, redirect
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
        forma = CommentForm(req.POST)
        if forma.is_valid():
            commentnew = Comment.objects.create()
            commentnew.name = req.POST.get('name')
            commentnew.body = req.POST.get('body')
            commentnew.kino = film
            commentnew.active = True
            commentnew.save()
            forma = CommentForm()
    data = {'forma': forma, 'commentsall': commentsall, 'kino': film}
    return render(req, 'film.html', context=data)
