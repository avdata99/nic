# Generated by Django 3.1.2 on 2020-10-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cambios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campocambio',
            name='uid_anterior',
            field=models.IntegerField(default=0, help_text='to be deleted after migration'),
        ),
    ]
