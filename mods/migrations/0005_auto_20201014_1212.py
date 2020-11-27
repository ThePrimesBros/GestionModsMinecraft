# Generated by Django 3.1.1 on 2020-10-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0004_auto_20201014_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mods',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='mods',
            name='last_maj',
        ),
        migrations.AddField(
            model_name='mods',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='mods',
            name='creator',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='mods',
            name='download',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mods',
            name='img',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
