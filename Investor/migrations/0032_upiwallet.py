# Generated by Django 3.0.8 on 2020-08-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investor', '0031_upi'),
    ]

    operations = [
        migrations.CreateModel(
            name='UPIwallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Choose_your_wallet', models.CharField(choices=[('1', 'PayTM'), ('2', 'BHIM Axis Pay'), ('3', 'PhonePe'), ('4', 'Mobikwik'), ('5', 'Amazon Pay')], max_length=1)),
            ],
        ),
    ]
