# Generated by Django 5.1.2 on 2024-11-10 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookdata', '0006_delete_personreference'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reference',
            options={'ordering': ('chapter',), 'verbose_name': 'Reference', 'verbose_name_plural': 'References'},
        ),
    ]
