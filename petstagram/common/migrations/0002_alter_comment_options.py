# Generated by Django 4.1.2 on 2022-11-15 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_time_publication']},
        ),
    ]
