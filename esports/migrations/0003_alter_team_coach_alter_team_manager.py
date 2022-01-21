# Generated by Django 4.0.1 on 2022-01-21 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esports', '0002_player_discord_player_twitch_player_twitter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_coach', to='esports.player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_manager', to='esports.player'),
        ),
    ]