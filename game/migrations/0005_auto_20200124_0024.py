# Generated by Django 2.2.9 on 2020-01-24 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20200124_0022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gameplayer',
            options={'ordering': ('game', 'name'), 'verbose_name_plural': 'Game Players'},
        ),
    ]
