from django.db import models


class Game(models.Model):
    STATUS_NEW = 'new'
    STATUS_RUNNING = 'run'
    STATUS_COMPLETED = 'comp'
    STATUS_CANCELLED = 'cxl'
    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_RUNNING, 'Running'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]
    name = models.CharField(
        max_length=64,
        help_text="Name of the game")
    status = models.CharField(
        max_length=4, choices=STATUS_CHOICES, default=STATUS_NEW,
        help_text="The status of the game",
        editable=False)
    num_rounds = models.PositiveSmallIntegerField(
        help_text="The number of rounds the game should last",
        default=10)

    def __str__(self):
        return "%s (%s)" % (self.name, self.status)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Games"
        unique_together = (
            ('name',),
        )


class GamePlayer(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE,
        help_text="The game being played")
    name = models.CharField(
        max_length=64,
        help_text="Name of the player")
    is_owner = models.BooleanField(
        help_text="Is this player the owner of the game",
        default=False)
    max_round = models.PositiveSmallIntegerField(
        help_text="The last round the player made it to",
        editable=False, default=1)

    def __str__(self):
        return "%s (%s)" % (self.name, self.game.name)

    class Meta:
        ordering = ('game', 'name',)
        verbose_name_plural = "Game Players"
        unique_together = (
            ('game', 'name',),
        )


class Trivia(models.Model):
    question = models.CharField(
        max_length=255,
        help_text="The trivia question")
    answer = models.CharField(
        max_length=128,
        help_text="The trivia answer")
    quess1 = models.CharField(
        max_length=128,
        help_text="A wrong guess")
    quess2 = models.CharField(
        max_length=128,
        help_text="Another wrong guess")

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('question',)
        verbose_name_plural = "Trivia"
        unique_together = (
            ('question'),
        )


class GameRound(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE,
        help_text="The provider account of the authorization",
        editable=False)
    round_number = models.PositiveSmallIntegerField(
        help_text="The round of the game",
        editable=False)
    trivia = models.ForeignKey(
        Trivia, on_delete=models.CASCADE,
        help_text="The trivia question",
        editable=False)

    def __str__(self):
        return "%s (round %d)" % (self.game, self.round_number)

    class Meta:
        ordering = ('game', 'round_number',)
        verbose_name_plural = "Game Rounds"
        unique_together = (
            ('game', 'round_number', 'trivia'),
        )
