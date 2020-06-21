# Generated by Django 3.0.5 on 2020-06-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_image_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_description',
        ),
        migrations.AddField(
            model_name='post',
            name='image_alt_text',
            field=models.TextField(default='No image alt text available'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_title',
            field=models.TextField(default='No image description title available'),
        ),
    ]