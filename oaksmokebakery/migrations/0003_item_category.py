# Generated by Django 4.1.5 on 2023-01-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaksmokebakery', '0002_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Bread', 'Bread'), ('Cake', 'Cake'), ('Pastries', 'Pastries'), ('Specialty Bread', 'Specialty Bread'), ('Ocassion Cake', 'Ocassion Cake')], max_length=25, null=True),
        ),
    ]