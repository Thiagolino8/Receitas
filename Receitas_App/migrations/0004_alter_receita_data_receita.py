# Generated by Django 3.2.6 on 2021-08-16 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receitas_App', '0003_auto_20210813_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 16, 15, 26, 8, 491753)),
        ),
    ]
