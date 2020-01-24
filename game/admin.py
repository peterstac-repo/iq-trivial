from django.contrib import admin

from game import models


admin.site.register(models.Game)
admin.site.register(models.GamePlayer)
admin.site.register(models.Trivia)
admin.site.register(models.GameRound)
