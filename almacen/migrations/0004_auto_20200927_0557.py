# Generated by Django 3.1.1 on 2020-09-27 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_auto_20200927_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.producto'),
        ),
    ]
