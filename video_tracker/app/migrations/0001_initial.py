# Generated by Django 4.0.3 on 2022-04-10 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('playlist_id', models.CharField(max_length=255)),
                ('thumbnail_url', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('views', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('youtube_id', models.CharField(max_length=255)),
                ('date_published', models.DateTimeField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.channel')),
            ],
        ),
    ]