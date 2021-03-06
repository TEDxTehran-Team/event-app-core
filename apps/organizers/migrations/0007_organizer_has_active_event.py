# Generated by Django 2.2 on 2020-12-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0006_organizer_main_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='has_active_event',
            field=models.BooleanField(default=False, help_text='Is there an active event for this organizer?', verbose_name='Has Active Event'),
        ),
    ]
