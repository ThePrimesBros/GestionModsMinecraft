# Generated by Django 3.1.1 on 2020-10-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0005_auto_20201014_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mods',
            name='creator',
            field=models.CharField(default='', max_length=255),
        ),
    ]