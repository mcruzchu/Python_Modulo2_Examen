# Generated by Django 4.2.7 on 2023-12-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesero',
            name='dni',
            field=models.CharField(default='00000000', max_length=8),
        ),
    ]
