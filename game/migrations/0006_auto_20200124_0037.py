# Generated by Django 2.2.9 on 2020-01-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20200124_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameplayer',
            name='is_owner',
            field=models.BooleanField(default=False, help_text='Is this player the owner of the game'),
        ),
    ]
