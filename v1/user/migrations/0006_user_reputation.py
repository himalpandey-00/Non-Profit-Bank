# Generated by Django 3.1.4 on 2021-01-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userbank_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reputation',
            field=models.IntegerField(default=100),
        ),
    ]