# Generated by Django 4.2.3 on 2023-09-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_name', models.CharField(max_length=100)),
                ('education_years', models.CharField(max_length=100)),
                ('education_address', models.CharField(max_length=100)),
                ('education_lvl', models.CharField(max_length=100)),
                ('education_description', models.TextField()),
            ],
        ),
    ]
