# Generated by Django 4.1.2 on 2022-11-24 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0009_room_occupancy"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="isBlocked",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="room",
            name="blockTimeEnd",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
