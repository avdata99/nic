# Generated by Django 3.1.2 on 2020-10-14 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zona',
            name='tz',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
