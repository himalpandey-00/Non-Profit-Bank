# Generated by Django 3.1.4 on 2021-01-19 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_bank_is_active'),
        ('user', '0003_userbank'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userbank',
            unique_together={('user', 'bank')},
        ),
    ]