# Generated by Django 4.1.3 on 2022-11-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_api', '0003_updated_notes_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
