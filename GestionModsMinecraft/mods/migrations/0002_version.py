# Generated by Django 3.1.1 on 2020-10-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='', max_length=30, null=True, unique=True)),
            ],
        ),
    ]