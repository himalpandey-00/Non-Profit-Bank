# Generated by Django 3.1.4 on 2021-01-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0007_auto_20210122_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
