# Generated by Django 4.2.6 on 2023-10-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_campusdon_options_remove_content_members_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campusdon',
            name='phone_number',
            field=models.CharField(default='000-000-0000', max_length=30),
        ),
    ]
