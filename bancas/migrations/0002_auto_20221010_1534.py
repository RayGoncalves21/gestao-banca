# Generated by Django 3.0 on 2022-10-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banca',
            name='data_registro_banca',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data inicio banca'),
        ),
        migrations.AlterField(
            model_name='banca',
            name='valor_da_entrada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='Valor da entrada'),
        ),
        migrations.AlterField(
            model_name='banca',
            name='valor_da_saida',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='Valor da Saída'),
        ),
    ]
