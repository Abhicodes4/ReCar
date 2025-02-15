# Generated by Django 5.0 on 2023-12-18 19:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recar', '0003_remove_cars_description_cars_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='ownership',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars',
            name='transmission',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='company',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
