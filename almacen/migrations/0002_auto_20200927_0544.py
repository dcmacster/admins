# Generated by Django 3.1.1 on 2020-09-27 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='maximo',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='minimo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='codigob',
        ),
        migrations.AddField(
            model_name='inventario',
            name='codigob',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='maximo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='minimo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.producto'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='almacen.producto'),
        ),
    ]
