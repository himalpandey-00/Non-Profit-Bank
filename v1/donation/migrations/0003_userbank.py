# Generated by Django 3.1.4 on 2021-01-21 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_auto_20210121_1557'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donation', '0002_auto_20210119_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField(choices=[(0, 'View'), (1, 'Create'), (2, 'Update'), (3, 'Delete')], default=1)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bank', to='bank.bank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]