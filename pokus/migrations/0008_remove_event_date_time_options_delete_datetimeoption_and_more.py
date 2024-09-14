# Generated by Django 4.1.7 on 2023-09-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokus", "0007_datetimeoption_remove_event_date_time_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="event", name="date_time_options",),
        migrations.DeleteModel(name="DateTimeOption",),
        migrations.AddField(
            model_name="event",
            name="date_time_options",
            field=models.DateTimeField(null=True),
        ),
    ]
