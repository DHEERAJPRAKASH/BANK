# Generated by Django 3.1.7 on 2021-08-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CUSTOMERS', '0004_auto_20210810_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='idd',
            field=models.IntegerField(default=0),
        ),
    ]