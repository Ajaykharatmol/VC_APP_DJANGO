# Generated by Django 3.0.8 on 2020-07-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Startup', '0004_founder_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startup_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Legal_Name_of_company', models.CharField(max_length=20)),
                ('Startup_Name', models.CharField(max_length=20)),
                ('Founding_month_and_year', models.IntegerField()),
                ('Location', models.CharField(max_length=20)),
                ('Sector', models.IntegerField()),
                ('Stage', models.IntegerField()),
                ('Upload_GST_certificate_or_License_for_verification', models.IntegerField()),
                ('Product_Summary', models.TextField()),
                ('Team_Summary', models.TextField()),
                ('Why_are_you_better_than_your_competitors_or_What_differentiates_you', models.TextField()),
                ('Upload_Pitch_deck', models.IntegerField()),
            ],
        ),
    ]
