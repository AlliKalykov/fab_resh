# Generated by Django 2.2.10 on 2021-12-09 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userquiz',
            old_name='user',
            new_name='user_quiz',
        ),
    ]
