# Generated by Django 5.0.4 on 2024-04-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_alter_listing_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='banner',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='banner',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]