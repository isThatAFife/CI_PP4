# Generated by Django 4.2.17 on 2024-12-12 04:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("gamelibrary", "0006_game_artwork_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="artwork_url",
            new_name="cover_url",
        ),
    ]