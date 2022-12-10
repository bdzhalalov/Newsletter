# Generated by Django 4.1.3 on 2022-12-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[(0, 'created'), (1, 'in_progress'), (2, 'sent'), (3, 'failed')], default=0, max_length=12),
        ),
    ]
