# Generated by Django 3.1.2 on 2020-11-28 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dominios', '0012_auto_20201124_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnsdominio',
            name='object_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dnsdominio',
            name='object_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='predominio',
            name='object_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predominio',
            name='object_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]