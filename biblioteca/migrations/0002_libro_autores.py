# Generated by Django 3.2.22 on 2023-10-10 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(to='biblioteca.Autor'),
        ),
    ]
