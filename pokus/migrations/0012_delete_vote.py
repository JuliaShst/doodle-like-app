# Generated by Django 5.0.3 on 2024-09-14 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pokus", "0011_vote"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Vote",
        ),
    ]
