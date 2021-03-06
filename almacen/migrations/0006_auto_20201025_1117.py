# Generated by Django 3.1.1 on 2020-10-25 17:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0005_regentrada_regsalida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='ID único para este producto', primary_key=True, serialize=False),
        ),
    ]
