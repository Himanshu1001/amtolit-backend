# Generated by Django 2.2.4 on 2019-08-18 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190818_1146'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Responders',
        ),
    ]