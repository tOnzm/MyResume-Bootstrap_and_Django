# Generated by Django 4.2.3 on 2023-09-01 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0002_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='experience_name',
            new_name='experience_company',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='experience_lvl',
            new_name='experience_role',
        ),
    ]
