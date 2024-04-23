# Generated by Django 5.0 on 2023-12-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recar', '0002_remove_cars_image_cars_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='description',
        ),
        migrations.AddField(
            model_name='cars',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic1'),
        ),
    ]
