# Generated by Django 5.0.1 on 2024-05-29 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('capacite', models.IntegerField()),
                ('batiment', models.CharField(max_length=100)),
            ],
        ),
    ]
