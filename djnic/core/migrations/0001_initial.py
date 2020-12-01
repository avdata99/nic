# Generated by Django 3.1.2 on 2020-12-01 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=50, help_text='0/100 priority level')),
                ('title', models.CharField(max_length=90)),
                ('description', models.TextField(blank=True, null=True)),
                ('object_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
