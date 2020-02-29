# Generated by Django 3.0.3 on 2020-02-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aula5', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('texto', models.TextField()),
                ('categorias', models.ManyToManyField(related_name='posts', to='aula5.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30)),
                ('comentario', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula5.Post')),
            ],
        ),
    ]
