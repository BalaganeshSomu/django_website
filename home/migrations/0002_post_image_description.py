# Generated by Django 3.0.5 on 2020-06-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_description',
            field=models.TextField(default='image description'),
        ),
    ]