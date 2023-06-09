# Generated by Django 4.2.2 on 2023-06-19 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_departamento_proyecto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleados.departamento'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleados.proyecto'),
        ),
    ]
