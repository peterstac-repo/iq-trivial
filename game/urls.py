from django.urls import path

from game import views


app_name = 'game'

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path("about/", views.About.as_view(), name='about'),

    path("games/", views.Games.as_view(), name='games'),
    path("games/<int:game_id>/", views.Game.as_view(), name='game'),
]
