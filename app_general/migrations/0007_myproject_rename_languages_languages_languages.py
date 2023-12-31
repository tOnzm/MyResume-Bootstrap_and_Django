# Generated by Django 4.2.3 on 2023-09-01 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0006_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myproject_name', models.CharField(max_length=100)),
                ('myproject_description', models.TextField()),
                ('myproject_image', models.ImageField(upload_to='app_cards/card_images')),
            ],
        ),
        migrations.RenameField(
            model_name='languages',
            old_name='Languages',
            new_name='languages',
        ),
    ]
