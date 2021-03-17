# Generated by Django 3.0 on 2021-03-15 17:52

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField(default='2021-03-15')),
                ('imagen', models.ImageField(upload_to='imagenes')),
                ('texto', ckeditor.fields.RichTextField(verbose_name='Texto')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Tipos')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
