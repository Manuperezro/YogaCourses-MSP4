# Generated by Django 3.2.13 on 2022-07-11 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_course_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='pricing_tiers',
        ),
    ]