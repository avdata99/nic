# Generated by Django 3.1.2 on 2020-10-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dominio',
            name='data_updated',
            field=models.DateTimeField(blank=True, help_text='When this record was updated', null=True),
        ),
    ]
