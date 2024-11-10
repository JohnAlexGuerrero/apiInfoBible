# Generated by Django 5.1.2 on 2024-11-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_remove_event_verses_event_verses'),
        ('person', '0004_character_tribe_genealogy'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='character',
            field=models.ManyToManyField(blank=True, null=True, to='person.character', verbose_name='characters'),
        ),
    ]
