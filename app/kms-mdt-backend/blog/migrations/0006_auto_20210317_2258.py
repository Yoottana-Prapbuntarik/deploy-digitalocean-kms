# Generated by Django 3.1.7 on 2021-03-17 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='own_uesr',
            new_name='own_user',
        ),
    ]
