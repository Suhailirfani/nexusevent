# Generated by Django 5.1.7 on 2025-03-15 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=100)),
                ('cus_phone', models.CharField(max_length=15)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('ev_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.event')),
            ],
        ),
    ]
