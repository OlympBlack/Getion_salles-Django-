# Generated by Django 5.0.1 on 2024-05-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='heure',
            field=models.CharField(choices=[('07h-10h', '07h-10h'), ('10h-12h', '10h-12h'), ('15h-17h', '15h-17h'), ('17h-19h', '17h-18h')], max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='jour',
            field=models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredo', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi')], max_length=400, null=True),
        ),
    ]
