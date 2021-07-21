# Generated by Django 3.2.5 on 2021-07-20 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0006_alter_curso_curso_publicado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='inscripciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField()),
                ('costo_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.curso')),
                ('estudiantes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
