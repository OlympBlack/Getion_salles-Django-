# Generated by Django 5.0.1 on 2024-05-29 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salle', '0002_remove_salle_nom_salle_numero_alter_salle_batiment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=10)),
                ('salle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salle.salle')),
            ],
        ),
    ]
