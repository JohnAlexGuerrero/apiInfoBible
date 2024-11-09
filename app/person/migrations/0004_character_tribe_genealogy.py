# Generated by Django 5.1.2 on 2024-11-08 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdata', '0006_delete_personreference'),
        ('person', '0003_remove_character_classification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='tribe',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Genealogy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('padre', 'Padre'), ('madre', 'Madre'), ('hijo(a)', 'Hijo'), ('esposo(a)', 'Esposa')], max_length=50)),
                ('character_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_1', to='person.character')),
                ('character_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_2', to='person.character')),
                ('verse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookdata.reference')),
            ],
            options={
                'verbose_name': 'Genealogy',
                'verbose_name_plural': 'Genealogies',
                'unique_together': {('character_1', 'character_2')},
            },
        ),
    ]