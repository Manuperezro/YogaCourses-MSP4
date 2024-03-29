# Generated by Django 3.2.13 on 2022-07-05 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('stripe_price_id', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default='defatul.png', upload_to='avatar'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('pricing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='accounts.pricing')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
