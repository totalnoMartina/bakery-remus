# Generated by Django 4.1.5 on 2023-01-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaksmokebakery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
