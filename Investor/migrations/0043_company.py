# Generated by Django 3.0.8 on 2020-08-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investor', '0042_remove_dashboard1_name_of_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=200)),
                ('Company_location', models.CharField(max_length=20)),
                ('Sector', models.IntegerField()),
            ],
        ),
    ]
