# Generated by Django 5.0 on 2023-12-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_game_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='files/gamecovers'),
        ),
    ]
