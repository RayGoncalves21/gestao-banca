# Generated by Django 3.0 on 2022-10-10 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20221010_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]
