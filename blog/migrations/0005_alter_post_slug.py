# Generated by Django 3.2.6 on 2024-06-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_authorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
