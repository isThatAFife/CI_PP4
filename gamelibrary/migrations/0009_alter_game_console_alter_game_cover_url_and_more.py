# Generated by Django 4.2.17 on 2024-12-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gamelibrary", "0008_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="console",
            field=models.CharField(default="PC", max_length=200),
        ),
        migrations.AlterField(
            model_name="game",
            name="cover_url",
            field=models.URLField(
                blank=True, default="static/images/default.webp", null=True
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="userscore",
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
