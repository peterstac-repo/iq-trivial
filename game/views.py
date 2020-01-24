from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django import views

from game import models


class About(views.View):
    def get(self, request):
        return render(request, 'game/about.html', {"version": "1.0.0"})


class Index(views.View):
    def get(self, request):
        return render(request, 'game/index.html', {})


@method_decorator(login_required, name='get')
class Game(views.View):

    def get(self, request, *args, **kwargs):
        game_id = kwargs.pop('game_id', None)
        game = get_object_or_404(models.Game, pk=game_id)
        players = models.GamePlayer.objects.order_by('name', )
        params = {}
        params.update(dict(
            game=game,
            players=players,
        ))
        return render(request, 'game/game.html', params)


@method_decorator(login_required, name='get')
class Games(views.View):

    def get(self, request, *args, **kwargs):
        games = models.Game.objects.order_by('name', )
        return render(
            request, 'game/games.html',
            {
                'games': games,
            })
