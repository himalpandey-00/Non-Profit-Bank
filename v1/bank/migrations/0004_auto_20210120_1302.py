# Generated by Django 3.1.4 on 2021-01-20 07:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_featuredbank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredbank',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
