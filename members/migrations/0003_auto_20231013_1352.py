# Generated by Django 3.2.21 on 2023-10-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20231013_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='continent',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='country',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='field_of_study',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='foundation_position',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='full_name',
            field=models.CharField(default='John Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='member',
            name='member_id',
            field=models.CharField(default='KF010', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='member',
            name='membership_status',
            field=models.CharField(default='Active', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='nick_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(default='000-000-0000', max_length=30),
        ),
        migrations.AddField(
            model_name='member',
            name='skills_expertise',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='member',
            name='state_district_city',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='year_joining_foundation',
            field=models.IntegerField(default=2022),
        ),
        migrations.AddField(
            model_name='member',
            name='year_joining_klymax',
            field=models.IntegerField(default=2022),
        ),
    ]
