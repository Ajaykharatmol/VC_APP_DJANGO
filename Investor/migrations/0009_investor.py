# Generated by Django 3.0.8 on 2020-07-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investor', '0008_investment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=20)),
                ('Date_of_birth', models.IntegerField()),
                ('Email_address', models.EmailField(max_length=254)),
                ('Contact_Number', models.IntegerField()),
            ],
        ),
    ]
