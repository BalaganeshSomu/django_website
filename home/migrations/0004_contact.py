# Generated by Django 3.0.5 on 2020-06-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200621_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('contact_number', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]