# Generated by Django 5.0.4 on 2024-05-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0005_booking_approximate_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='approximate_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
