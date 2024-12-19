from django.db import migrations
from django.utils.dateparse import parse_date

def convert_string_to_date(apps, schema_editor):
    Game = apps.get_model('gamelibrary', 'Game')
    for game in Game.objects.all():
        try:
            game.date = parse_date(game.date)
            game.save()
        except ValueError:
            print(f"Invalid date string: {game.date}")

class Migration(migrations.Migration):

    dependencies = [
        ('gamelibrary', '0010_game_newdate_alter_game_cover_url_alter_game_date'),
    ]

    operations = [
        migrations.RunPython(convert_string_to_date),
    ]
