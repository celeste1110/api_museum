# Generated by Django 4.0.5 on 2022-06-23 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_museum', '0004_alter_museum_lat_alter_museum_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='image',
            field=models.ImageField(null=True, upload_to='museums'),
        ),
        migrations.CreateModel(
            name='CulturalProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mame', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='properts')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_museum.artist')),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_museum.medium')),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_museum.museum')),
            ],
        ),
    ]
