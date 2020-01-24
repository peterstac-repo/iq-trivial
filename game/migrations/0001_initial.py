# Generated by Django 2.2.9 on 2020-01-23 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the game', max_length=64)),
                ('status', models.CharField(choices=[('new', 'New'), ('run', 'Running'), ('comp', 'Completed'), ('cxl', 'Cancelled')], default='new', editable=False, help_text='The status of the game', max_length=4)),
                ('num_rounds', models.PositiveSmallIntegerField(default=10, help_text='The number of rounds the game should last')),
            ],
            options={
                'verbose_name_plural': 'Games',
                'ordering': ('name',),
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='The trivia question', max_length=255)),
                ('answer', models.CharField(help_text='The trivia answer', max_length=128)),
                ('quess1', models.CharField(help_text='A wrong guess', max_length=128)),
                ('quess2', models.CharField(help_text='Another wrong guess', max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Trivia',
                'ordering': ('question',),
                'unique_together': {('question',)},
            },
        ),
        migrations.CreateModel(
            name='GameRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.PositiveSmallIntegerField(editable=False, help_text='The round of the game')),
                ('game', models.ForeignKey(editable=False, help_text='The provider account of the authorization', on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('trivia', models.ForeignKey(editable=False, help_text='The trivia question', on_delete=django.db.models.deletion.CASCADE, to='game.Trivia')),
            ],
            options={
                'verbose_name_plural': 'Game Rounds',
                'ordering': ('game', 'round_number'),
                'unique_together': {('game', 'round_number', 'trivia')},
            },
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the player', max_length=64)),
                ('is_owner', models.BooleanField(editable=False, help_text='Is this player the owner of the game')),
                ('max_round', models.PositiveSmallIntegerField(editable=False, help_text='The last round the player made it to')),
                ('game', models.ForeignKey(editable=False, help_text='The game being played', on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
            ],
            options={
                'verbose_name_plural': 'Game Players',
                'ordering': ('name',),
                'unique_together': {('game', 'name')},
            },
        ),
    ]