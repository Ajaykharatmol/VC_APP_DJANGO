# Generated by Django 3.0.8 on 2020-08-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investor', '0017_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_details',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(blank=True, upload_to='profile_images/'),
        ),
    ]
