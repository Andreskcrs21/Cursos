# Generated by Django 3.2.5 on 2021-07-20 23:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_curso_curso_publicado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inscripciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='inscripciones',
            new_name='Inscripcion',
        ),
        migrations.RenameField(
            model_name='inscripcion',
            old_name='estudiantes',
            new_name='estudiante',
        ),
    ]
