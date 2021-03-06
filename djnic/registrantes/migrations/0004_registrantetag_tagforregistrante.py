# Generated by Django 3.1.2 on 2020-11-28 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrantes', '0003_auto_20201128_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagForRegistrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=190)),
                ('object_created', models.DateTimeField(auto_now_add=True)),
                ('object_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistranteTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_created', models.DateTimeField(auto_now_add=True)),
                ('object_modified', models.DateTimeField(auto_now=True)),
                ('registrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrantes.registrante')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrantes.tagforregistrante')),
            ],
        ),
    ]
