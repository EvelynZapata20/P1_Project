# Generated by Django 3.2.8 on 2023-08-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doggy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vet',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
