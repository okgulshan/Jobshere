# Generated by Django 5.0.4 on 2024-04-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_joblisting'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
    ]