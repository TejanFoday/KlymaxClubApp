# Generated by Django 3.2.21 on 2023-10-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='membership_status',
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
