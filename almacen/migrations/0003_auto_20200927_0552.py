# Generated by Django 3.1.1 on 2020-09-27 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_auto_20200927_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='almacen.producto'),
        ),
    ]
