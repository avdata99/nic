# Generated by Django 3.1.2 on 2020-11-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnss', '0004_auto_20201128_0950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=90, unique=True),
        ),
    ]
