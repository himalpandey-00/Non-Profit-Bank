# Generated by Django 3.1.4 on 2021-01-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_auto_20210120_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='description',
            field=models.TextField(),
        ),
    ]
