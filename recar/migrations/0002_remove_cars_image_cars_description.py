# Generated by Django 5.0 on 2023-12-18 17:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='image',
        ),
        migrations.AddField(
            model_name='cars',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
