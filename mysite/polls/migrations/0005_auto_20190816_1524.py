# Generated by Django 2.2.4 on 2019-08-16 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_auto_20190816_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='poll_orderid_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='poll_orderid_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='poll_orderid_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='textanswer',
            name='answer',
            field=models.TextField(default='Answer'),
        ),
        migrations.CreateModel(
            name='Responders',
            fields=[
                ('commeninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='polls.CommenInfo')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
                ('responder', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('polls.commeninfo',),
        ),
    ]