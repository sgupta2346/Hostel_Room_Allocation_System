# Generated by Django 4.1.2 on 2022-11-24 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0012_remove_room_blocktimeend"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="blockTimeEnd",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
