# Generated by Django 3.0 on 2022-10-10 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='login',
            new_name='username',
        ),
    ]
