# Generated by Django 5.1.3 on 2024-11-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserService', '0002_userprofile_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
    ]