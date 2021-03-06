# Generated by Django 3.1.2 on 2020-10-12 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dominios', '0004_dominio_changes_migrated'),
    ]

    operations = [
        migrations.CreateModel(
            name='CambiosDominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('dominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cambios', to='dominios.dominio')),
            ],
        ),
        migrations.CreateModel(
            name='CampoCambio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.CharField(max_length=240, null=True)),
                ('anterior', models.CharField(max_length=240, null=True)),
                ('nuevo', models.CharField(max_length=240, null=True)),
                ('cambio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campos', to='cambios.cambiosdominio')),
            ],
        ),
    ]
