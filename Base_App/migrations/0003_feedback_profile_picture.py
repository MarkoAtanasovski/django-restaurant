# Generated by Django 5.2.1 on 2025-06-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0002_alter_booktable_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='profile_picture',
            field=models.ImageField(default='default_profile.jpg', upload_to='feedback_pics/'),
        ),
    ]
