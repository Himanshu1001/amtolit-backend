# Generated by Django 2.2.4 on 2019-08-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_phoneotp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
