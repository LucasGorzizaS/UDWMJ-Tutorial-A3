# Generated by Django 4.1 on 2023-11-24 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialnetworks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('address', models.CharField(max_length=200, verbose_name='Endereco')),
                ('cell_phone', models.CharField(max_length=20, verbose_name='Telefone celular')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ClientSocialnetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('socialnetwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialnetworks.socialnetwork')),
            ],
            options={
                'verbose_name': 'Item de Redes Social',
                'verbose_name_plural': 'Itens de Rede Social',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='client',
            name='client_socialnetwork',
            field=models.ManyToManyField(blank=True, through='clients.ClientSocialnetwork', to='socialnetworks.socialnetwork'),
        ),
    ]
