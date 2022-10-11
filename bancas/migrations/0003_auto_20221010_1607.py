# Generated by Django 3.0 on 2022-10-10 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bancas', '0002_auto_20221010_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bancas_uma_pra_uma',
            fields=[
                ('bancas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bancas.Banca')),
            ],
        ),
        migrations.RemoveField(
            model_name='banca',
            name='valor_da_entrada',
        ),
        migrations.RemoveField(
            model_name='banca',
            name='valor_da_saida',
        ),
        migrations.CreateModel(
            name='Banca_entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_da_entrada', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='Valor da entrada')),
                ('selecionar_banca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bancas.Banca', verbose_name='Selecione a banca')),
            ],
            options={
                'verbose_name': ('Banca entrada',),
                'verbose_name_plural': ('Entradas Bancas',),
                'db_table': 'banca_entrada',
            },
        ),
    ]
