# Generated by Django 3.1.4 on 2020-12-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='secureuser',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
