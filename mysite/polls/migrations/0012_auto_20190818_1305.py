# Generated by Django 2.2.4 on 2019-08-18 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_textanswer_question_poll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_poll',
            new_name='poll',
        ),
        migrations.RenameField(
            model_name='textanswer',
            old_name='question_poll',
            new_name='poll',
        ),
    ]
