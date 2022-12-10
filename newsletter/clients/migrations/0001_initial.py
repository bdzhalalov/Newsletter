# Generated by Django 4.1.3 on 2022-12-01 09:06

import clients.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11, validators=[clients.validators.validate_number])),
                ('code', models.CharField(max_length=3)),
                ('tag', models.CharField(max_length=26)),
                ('timezone', models.DateTimeField()),
            ],
        ),
    ]
