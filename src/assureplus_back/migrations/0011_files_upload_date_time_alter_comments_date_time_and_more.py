# Generated by Django 4.1.7 on 2023-04-01 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assureplus_back', '0010_sinistres_remove_comments_sinitre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='files_upload',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='sinistres',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]