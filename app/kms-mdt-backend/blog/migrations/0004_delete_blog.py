# Generated by Django 3.1.7 on 2021-03-17 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_uesr'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
