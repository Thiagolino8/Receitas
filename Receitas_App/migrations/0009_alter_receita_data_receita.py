# Generated by Django 3.2.5 on 2021-10-22 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receitas_App', '0008_auto_20210817_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 22, 0, 46, 56, 311004)),
        ),
    ]
