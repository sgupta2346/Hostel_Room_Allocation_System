# Generated by Django 4.1.2 on 2022-11-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0006_alter_room_occupancy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room", name="occupancy", field=models.PositiveIntegerField(),
        ),
    ]
