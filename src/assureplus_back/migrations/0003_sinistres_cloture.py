# Generated by Django 4.1.7 on 2023-04-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assureplus_back', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinistres',
            name='cloture',
            field=models.BooleanField(default=False),
        ),
    ]