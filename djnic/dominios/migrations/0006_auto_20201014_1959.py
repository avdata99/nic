# Generated by Django 3.1.2 on 2020-10-14 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominios', '0005_dominio_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominio',
            name='uid_anterior',
            field=models.IntegerField(db_index=True, default=0, help_text='to be deleted after migration'),
        ),
    ]
