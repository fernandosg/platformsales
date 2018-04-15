# Generated by Django 2.0.4 on 2018-04-13 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('puntoenlace', '__first__')
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=12)),
                ('contrasena', models.CharField(max_length=10)),
                ('fecha_instalacion', models.DateTimeField()),
                ('is_activo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PagoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='cliente.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='cliente.Departamento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='puntoenlace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puntoenlaces', to='puntoenlace.PuntoEnlace'),
        ),
    ]
