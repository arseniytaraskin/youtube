# Generated by Django 4.2.1 on 2023-06-10 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='author',
            new_name='user',
        ),
    ]