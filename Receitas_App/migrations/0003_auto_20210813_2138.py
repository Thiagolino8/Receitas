# Generated by Django 3.2.6 on 2021-08-14 00:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receitas_App', '0002_alter_receita_data_receita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='categora',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 13, 21, 38, 36, 533752)),
        ),
    ]
