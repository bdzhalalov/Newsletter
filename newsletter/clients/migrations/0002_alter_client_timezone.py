# Generated by Django 4.1.3 on 2022-12-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='timezone',
            field=models.CharField(max_length=32),
        ),
    ]
