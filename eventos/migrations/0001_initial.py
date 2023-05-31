# Generated by Django 4.2.1 on 2023-05-30 20:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('diploma', models.BooleanField(default=0)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField(default=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
