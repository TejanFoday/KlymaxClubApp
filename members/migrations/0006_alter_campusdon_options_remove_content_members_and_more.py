# Generated by Django 4.2.6 on 2023-10-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_campusdon_remove_member_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campusdon',
            options={'verbose_name': 'Campus Don', 'verbose_name_plural': 'Campus Dons'},
        ),
        migrations.RemoveField(
            model_name='content',
            name='members',
        ),
        migrations.RemoveField(
            model_name='event',
            name='members',
        ),
        migrations.AddField(
            model_name='member',
            name='email_address',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='campusdon',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='campusdon',
            name='nick_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
