# Generated by Django 5.0.4 on 2024-04-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='responsibilities',
            field=models.TextField(blank=True),
        ),
    ]