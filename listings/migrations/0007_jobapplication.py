# Generated by Django 5.0.4 on 2024-04-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_contactus_reportissue'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('companies', models.TextField()),
                ('ques1', models.TextField()),
                ('ques2', models.TextField()),
                ('ques3', models.TextField()),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]
