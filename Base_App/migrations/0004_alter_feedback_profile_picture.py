# Generated by Django 5.2.1 on 2025-06-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0003_feedback_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='profile_picture',
            field=models.ImageField(default='feedback_pics/default_avatar.jpg', upload_to='feedback_pics/'),
        ),
    ]
