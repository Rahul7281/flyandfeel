# Generated by Django 4.1.2 on 2024-12-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='summary_image',
            field=models.ImageField(blank=True, null=True, upload_to='summary_images/'),
        ),
    ]
