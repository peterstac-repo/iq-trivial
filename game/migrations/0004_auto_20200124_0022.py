# Generated by Django 2.2.9 on 2020-01-24 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20200124_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameplayer',
            name='game',
            field=models.ForeignKey(help_text='The game being played', on_delete=django.db.models.deletion.CASCADE, to='game.Game'),
        ),
    ]
