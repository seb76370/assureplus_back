# Generated by Django 4.1.7 on 2023-04-01 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assureplus_back', '0011_files_upload_date_time_alter_comments_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]