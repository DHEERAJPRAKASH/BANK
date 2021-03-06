# Generated by Django 3.1.7 on 2021-08-13 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('balance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='transfer_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('amount', models.FloatField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='CUSTOMERS.customer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='CUSTOMERS.customer')),
            ],
        ),
    ]
