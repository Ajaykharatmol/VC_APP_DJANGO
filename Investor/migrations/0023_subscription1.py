# Generated by Django 3.0.8 on 2020-08-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investor', '0022_administator_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
                ('Description', models.TextField(max_length=20)),
            ],
        ),
    ]
