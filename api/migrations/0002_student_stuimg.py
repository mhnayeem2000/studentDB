# Generated by Django 5.0.6 on 2025-04-04 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stuImg',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
    ]
