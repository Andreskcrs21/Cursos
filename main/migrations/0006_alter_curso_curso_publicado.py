# Generated by Django 3.2.5 on 2021-07-20 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210716_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 20, 15, 50, 3, 833020), verbose_name='Fecha de publicacion'),
        ),
    ]
