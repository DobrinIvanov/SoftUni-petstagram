# Generated by Django 4.1.2 on 2022-11-15 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('date_time_publication', models.DateTimeField(auto_now_add=True)),
                ('to_photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.photo')),
            ],
            options={
                'ordering': ['-date_time_publication'],
            },
        ),
    ]
