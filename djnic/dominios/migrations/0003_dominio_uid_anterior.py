# Generated by Django 3.1.2 on 2020-10-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominios', '0002_dominio_data_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='dominio',
            name='uid_anterior',
            field=models.IntegerField(default=0, help_text='to be deleted after migration'),
        ),
    ]