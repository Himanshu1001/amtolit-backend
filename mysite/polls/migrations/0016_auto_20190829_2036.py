# Generated by Django 2.2.4 on 2019-08-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20190829_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='background_color',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
