# Generated by Django 4.0.5 on 2022-06-23 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_museum', '0003_museum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='lon',
            field=models.FloatField(null=True),
        ),
    ]
