# Generated by Django 5.0.1 on 2024-05-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0002_cours_heure_cours_jour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='jour',
            field=models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi')], max_length=400, null=True),
        ),
    ]
