# Generated by Django 3.2.13 on 2022-07-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220705_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
