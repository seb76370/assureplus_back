# Generated by Django 4.1.7 on 2023-03-30 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assureplus_back', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='users',
        ),
        migrations.RemoveField(
            model_name='files_upload',
            name='users',
        ),
        migrations.CreateModel(
            name='Sinitres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sinitres', to='assureplus_back.users')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='sinitres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='assureplus_back.sinitres'),
        ),
        migrations.AddField(
            model_name='files_upload',
            name='sinitres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files_upload', to='assureplus_back.sinitres'),
        ),
    ]