# Generated by Django 3.1.4 on 2021-01-21 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_auto_20210121_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'permissions': (('can_add', 'Can Add Bank'), ('can_add_edit', 'Can Add Edit Bank'), ('can_add_edit_delete', 'Can Add Edit Delete Bank'))},
        ),
    ]
