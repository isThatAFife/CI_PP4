import json
from django.db import migrations
import os
from django.utils.dateparse import parse_date
from datetime import datetime

def update_date_field(apps, schema_editor):
    Game = apps.get_model('gamelibrary', 'Game')
    fixture_file = os.path.join('gamelibrary/fixtures/games.json')
    
    with open(fixture_file, 'r') as file:
        fixtures = json.load(file)
        for fixture in fixtures:
            if fixture['model'] == 'gamelibrary.game':
                name = fixture['fields']['name']
                console = fixture['fields']['console']
                date_str = fixture['fields']['date']
                try:
                    games = Game.objects.filter(name=name, console=console)
                    if games.exists():
                        # Parse the date string
                        date_obj = datetime.strptime(date_str, '%b %d, %Y').date()
                        for game in games:
                            game.date = date_obj
                            game.save(update_fields=['date'])
                        print(f"Updated date for {name} on {console}")
                    else:
                        print(f"Game '{name}' for {console} not found")
                except ValueError:
                    print(f"Invalid date format for {name}: {date_str}")

class Migration(migrations.Migration):

    dependencies = [
        ('gamelibrary', '0012_alter_game_date'),
    ]

    operations = [
        migrations.RunPython(update_date_field),
    ]
