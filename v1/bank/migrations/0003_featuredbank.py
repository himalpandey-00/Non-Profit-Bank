# Generated by Django 3.1.4 on 2021-01-20 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_bank_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bank')),
            ],
        ),
    ]