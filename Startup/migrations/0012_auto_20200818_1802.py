# Generated by Django 3.0.8 on 2020-08-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Startup', '0011_auto_20200817_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='startup_details1',
            name='Administators_of_your_VC',
        ),
        migrations.RemoveField(
            model_name='startup_details1',
            name='Employees_of_your_VC',
        ),
    ]
