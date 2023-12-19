# Generated by Django 5.0 on 2023-12-17 07:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(related_name='tagged_games', to='main_app.tag'),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='games',
            field=models.ManyToManyField(related_name='game_lists', to='main_app.game'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
                ('created_at', models.DateTimeField()),
                ('likes', models.PositiveIntegerField()),
                ('dislikes', models.PositiveIntegerField()),
                ('score', models.IntegerField()),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='GameListItem',
        ),
    ]