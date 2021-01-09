# Generated by Django 3.1.2 on 2021-01-08 23:36

from django.db import migrations, models, transaction
import uuid


def gen_uuid(apps, schema_editor, model_real_name):
    MyModel = apps.get_model('registrantes', model_real_name)
    c = 0
    while MyModel.objects.filter(uid__isnull=True).exists():
        c += 1
        print('model_real_name: {} = {}'.format(model_real_name, c))
        with transaction.atomic():
            for row in MyModel.objects.filter(uid__isnull=True)[:1000]:
                row.uuid = uuid.uuid4()
                row.save(update_fields=['uid'])


def update_registrante(apps, schema_editor):
    gen_uuid(apps, schema_editor, model_real_name='Registrante')


def update_rt(apps, schema_editor):
    gen_uuid(apps, schema_editor, model_real_name='RegistranteTag')


def update_tr(apps, schema_editor):
    gen_uuid(apps, schema_editor, model_real_name='TagForRegistrante')


class Migration(migrations.Migration):

    dependencies = [
        ('registrantes', '0005_auto_20201128_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrante',
            name='uid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(update_registrante, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='registrante',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),

        migrations.AddField(
            model_name='registrantetag',
            name='uid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(update_rt, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='registrantetag',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),

        migrations.AddField(
            model_name='tagforregistrante',
            name='uid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(update_tr, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='tagforregistrante',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),

    ]