# Generated by Django 3.2.6 on 2021-10-24 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=15)),
                ('fechaexpedicion', models.DateField()),
                ('fechavencimiento', models.DateField()),
                ('categoria', models.CharField(max_length=10)),
                ('rh', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('restricciones', models.CharField(max_length=30)),
                ('organismotransitoexpididor', models.CharField(max_length=40)),
                ('fotolicencia', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'licencia',
                'verbose_name_plural': 'licencias',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=7)),
                ('correo', models.EmailField(max_length=254)),
                ('fechaexpediciondocumento', models.DateField()),
                ('fechanacimiento', models.DateField()),
                ('contraseña', models.CharField(max_length=30)),
                ('idlicencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedatos.licencia')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=5)),
                ('modelo', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('SOAT', models.FileField(upload_to='archivos/')),
                ('tecnicomecanica', models.FileField(upload_to='archivos/')),
                ('servicio', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=20)),
                ('VIM', models.IntegerField()),
                ('prendas', models.FileField(upload_to='archivos/')),
                ('tipocombustible', models.CharField(max_length=15)),
                ('historial', models.FileField(upload_to='archivos/')),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedatos.usuario')),
            ],
            options={
                'verbose_name': 'vehiculo',
                'verbose_name_plural': 'vehiculos',
            },
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numtramite', models.CharField(max_length=15)),
                ('nombretramite', models.CharField(max_length=15)),
                ('tipo', models.CharField(max_length=15)),
                ('duracion', models.CharField(max_length=15)),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedatos.usuario')),
                ('idvehiculo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basedatos.vehiculo')),
            ],
            options={
                'verbose_name': 'tramite',
                'verbose_name_plural': 'tramites',
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellidos', models.CharField(max_length=15)),
                ('idadministrador', models.CharField(max_length=15)),
                ('cargo', models.CharField(max_length=15)),
                ('idtramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedatos.tramite')),
            ],
            options={
                'verbose_name': 'administrador',
                'verbose_name_plural': 'administradores',
            },
        ),
    ]
