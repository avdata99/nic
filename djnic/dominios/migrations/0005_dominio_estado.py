# Generated by Django 3.1.2 on 2020-10-14 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominios', '0004_dominio_changes_migrated'),
    ]

    operations = [
        migrations.AddField(
            model_name='dominio',
            name='estado',
            field=models.CharField(db_index=True, max_length=90, null=True),
        ),
    ]
