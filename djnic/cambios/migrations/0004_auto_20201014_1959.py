# Generated by Django 3.1.2 on 2020-10-14 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cambios', '0003_auto_20201013_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campocambio',
            name='uid_anterior',
            field=models.IntegerField(db_index=True, default=0, help_text='to be deleted after migration'),
        ),
    ]
