# Generated by Django 3.2.13 on 2022-12-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=100)),
                ('song_url', models.CharField(max_length=400)),
                ('song_thumbnail', models.CharField(max_length=400)),
                ('song_runtime', models.CharField(max_length=10)),
            ],
        ),
    ]
